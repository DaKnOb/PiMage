# PiMage
Pi, as an Image

PiMage is a Python utility that will read an arbitralily long text file containing
Pi to as many decimal digits as possible and then will generate an image where each
pixel is colored based on a specific series of digits.

## How are colors calculated:
Each pixel has a color which contains one of the `256^3=16.8M` available combinations
using the RGB System with one byte per color. Pi is read 9 digits at a time. A pixel's
red value is determined by calculating the modulo of this number with `256`, which means
it can take any value between 0 and 255. The next three digits are used for green, and
finally the last three are used for blue.

## Example Outputs
The first 100,000 digits of Pi:

![100k Pi Digits](output/pi-pi-100000.txt.png)

The first 1,000,000 digits of Pi:

![1M Pi Digits](output/pi-pi-1000000.txt.png)
