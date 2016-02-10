[![](https://cloud.githubusercontent.com/assets/1317406/12406044/32cd9916-be0f-11e5-9b18-1547f284f878.png)](http://www.synapse-wireless.com/)

# Pyduino LCD Shield SNAPpy Library

`pyduino-lcd` is a SNAPpy library that makes it easy to develop applications for the Pyduino that use an LCD shield.

The [SparkFun LCD Button Shield](https://www.sparkfun.com/products/13293) is highly recommended
because it works very well with the Pyduino and this library.

## Installation

### For use in Portal

Download and extract the latest release zip file to Portal's `snappyImages` directory. 
By default, this is located at `..\Documents\Portal\snappyImages` on Windows.

### For use with SNAPbuild

The easiest way to install `pyduino-lcd` for use with SNAPbuild is using 
[pip](https://pip.pypa.io/en/latest/installing.html):

    pip install git+https://github.com/synapse-wireless/pyduino-lcd.git@master --process-dependency-links

Alternatively you can clone or download and extract the source, and install it:

    pip install ./pyduino-lcd --process-dependency-links
