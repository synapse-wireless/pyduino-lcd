# Pyduino LCD Shield SNAPpy Library

## Introduction

`pyduino-lcd` is a SNAPpy library that makes it easy to develop applications for the Pyduino that use an LCD shield.

The [SparkFun LCD Button Shield](https://www.sparkfun.com/products/13293) works very well with the Pyduino and this library and is highly recommended. 

Installation
------------

The easiest way to install `pyduino-lcd` is using 
[pip](https://pip.pypa.io/en/latest/installing.html):

    pip install git+ssh://git@git.synapse-wireless.com/tyler.crumpton/pyduino-lcd.git@master

Alternatively you can download the source, extract it, and install it:

    python setup.py install
    
(Eventually the package will be pushed to our pip repo, and won't require GitLab access.)

<!-- Commented out for now
Usage
-------------

In order to use the nice IO names, simply import `pyduino-includes` in your SNAPpy script like this:

```python
from PyduinoIncludes import *
    
def drive_d4_pin_high():
    setPinDir(D4, True)
    writePin(D4, True)
```

Pins can be referenced as follows:

| Pin Type | Pyduino IO Name |
|----------|-----------------|
| Digital  | D0 - D13        |
| Analog   | A0 - A5         |
| i2c      | SDA, SCL        |

Setting up the SPI pins is very simple, too:

```python
from PyduinoIncludes.SPI import *

def my_spi_function():
    spi_init()  # Sets up the bit-banged SPI
    spi_write("\x12\x34\x56")  # Write data to the SPI bus
    spi_read(4)  # Read four bytes from the SPI bus
```i

-->

