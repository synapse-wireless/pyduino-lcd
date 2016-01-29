"""Pyduino LCB shield library
Button ratio values are currently setup for Sparkfun button shield V2

Note: These ADC calculates can be recalculated for other shields resistor
      values if necessary.

Ex.
  #Initialize the LED and write hello world to the display
  lcd_init_io()
  lcd_init()
  
  clear_screen()
  write_line1('Hello World')
  
Ex.
  #Write the button that is currently being pressed to the display
  lcd_init_io()
  lcd_init()
  
  @setHook(HOOK_100MS)
  def show_button():
      clear_screen()
      write_line1(check_button())
  
"""

from PyduinoIO import *
from atmega128rfa1_math import *

# Pin definitions for LCD button shield
LCD_RS = D8
LCD_ENABLED = D9
DATAPINS = [D4, D5, D6, D7]
LCD_BACKLIGHT = D10
   
def lcd_init_io():
    """Initialize IO for LCD shield"""
    setPinDir(LCD_BACKLIGHT, True)
    setPinDir(LCD_RS, True)
    setPinDir(LCD_ENABLED, True)
    setPinDir(D4, True)
    setPinDir(D5, True)
    setPinDir(D6, True)
    setPinDir(D7, True)
    setPinDir(D7, True)
    
    writePin(LCD_BACKLIGHT, True)
    writePin(LCD_RS, True)
    writePin(LCD_ENABLED, False)
    writePin(D4, True)
    writePin(D5, True)
    writePin(D6, True)
    writePin(D7, True)
    
def lcd_init():
    """Send initialization commands to LCD and calibrate buttons"""
    # If plugged in USB, button offsets must be calibrated due to voltage tolerance
    global BUTTON_ADC
    global BUTTON_LEN
    BUTTON_LEN = 6
    BUTTON_ADC = [0x00] * BUTTON_LEN*2
    calibrate_buttons()
    
    command(0x33)
    command(0x32)
    command(0x28) #// 4 bit mode
    command(0x0C) 
    command(0x01) #// clear the screen
    command(0x06) #// increment cursor
    command(0x80) #// row 1 column 1

def command(data):
    """Send command to LCD"""
    writePin(LCD_RS, False)
    pulsePin(-1,-100, False)
    write4bits(data>>4)
    write4bits(data)
    
def write4bits(bits):
    """Send 4 bits of data to LCD via 4-bit parallel interface"""
    for pins in xrange(0,4):
        writePin(DATAPINS[pins], (bits>>pins)&0x01)
    pulsePin(LCD_ENABLED, -1000, True)
    
def write_line1(myStr):
    """Write data to line 1 of LCD screen"""
    command(0x80)  #// row 1 column 1
    writePin(LCD_RS, True)
    for byte in myStr:
        write4bits(ord(byte)>>4)
        write4bits(ord(byte))
    
def write_line2(myStr):
    """Write data to line 2 of LCD screen"""
    command(0xC0)  #// row 2 column 1
    writePin(LCD_RS, True)
    for byte in myStr:
        write4bits(ord(byte)>>4)
        write4bits(ord(byte))

def clear_screen():
    """Clear the LCD screen"""
    command(0x01)

last_button = 1023
def check_any_button():
    """Check to see if any button has changed state"""
    global last_button
    value = readAdc(A0)
    if last_button >= 950:
        if value < 950:
            last_button = value
            return True
    last_button = value

def read_button():
    return readAdc(A0)

def check_button():
    """Determine which button is being pressed"""
    ret_text = ''
    value = readAdc(A0)
    for btn in xrange(0, BUTTON_LEN):
        if abs(value - return_button_adc(btn)) < BUTTON_ERROR:
            ret_text = BUTTONS[btn]
            break
    return ret_text

def abs(value):
    """Calculate absolute value"""
    if value < 0:
        return -value
    return value

def return_button_adc(index):
    """Return the ADC ticks for an associated button"""
    index*=2
    adc_high = BUTTON_ADC[index] << 8
    adc_low = BUTTON_ADC[index+1]
    return adc_high | adc_low
    
def sense_5V():
    """Return the 5V bus voltage"""
    sense =  itos(readAdc(SENSE_5V))
    sense = mult_32(sense, '\x00\x00\x27\x10')
    sense = div_32 (sense, '\x00\x00\x07\x82')
    return stoi(sense) # mV

def sense_adc_max():
    """Return the maximum ADC reading as a ratio of the current bus voltage"""
    ratio =  itos(readAdc(SENSE_5V))
    ratio = mult_32(ratio, '\x00\x00\x27\x10')
    ratio = div_32 (ratio, '\x00\x00\x24\xB8')
    return stoi(ratio)

def calibrate_buttons():
    """Calibration mechanism to account for voltage variation on USB bus"""
    global BUTTON_ADC
    
    max = readAdc(A0)
    BUTTON_ADC[0] = max >> 8
    BUTTON_ADC[1] = max & 0xFF
    
    readAdc(SENSE_5V)
    max = itos(sense_adc_max()) # max adc

    for i in xrange(1, BUTTON_LEN):
        adc_ticks = stoi(div_32(mult_32(max, BUTTON_RATIO[i]), '\x00\x00\x27\x10'))
        BUTTON_ADC[i*2] = adc_ticks >> 8
        BUTTON_ADC[i*2+1] = adc_ticks & 0xFF
    

# ADC lookup table to translate adc to button presses
BUTTONS = ('', 'Up', 'Down', 'Left', 'Right', 'Select')

# Determine button ratio from maximum (Sparkfun button shield V2)
# up ratio = 10,000/8900
# down ratio = 10,000/8641
# left ratio = 10,000/8191
# up+down ratio = 10,000/7904
# right ratio = 10,000/7809
# up+left ratio = 10,000/7522
# down+left ratio = 10,000/7330
# up+right ratio = 10,000/7187
# select ratio = 10,000/5904

# Divider ratios
BUTTON_RATIO = ('','\x00\x00\x22\xc4', '\x00\x00\x21\xc1', '\x00\x00\x1f\xff', '\x00\x00\x1e\x81', \
                '\x00\x00\x17\x10')
# The adc reading must be within 6 ticks in order to determine the button selection
BUTTON_ERROR = 10