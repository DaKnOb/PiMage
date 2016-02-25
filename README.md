# PiMage
Pi, as an Image

PiMage is a Python utility that will read an arbitralily long text file containing
Pi to as many decimal digits as possible and then will generate an image where each
pixel is colored based on its digits.

## How are colors calculated:
All colors are grayscale which means their Red, Green, and Blue values are equal. The
value is calculated by multiplying each digit by 28. For example, the digit 0 becomes
`(0,0,0)`, the digit 1 becomes `(28,28,28)` and the digit 9 becomes `(252,252,252)`.

## Example Outputs
The first 100,000 digits of Pi:

![100k Pi Digits](output/pi-pi-100000.txt.png)

The first 1,000,000 digits of Pi:

![1M Pi Digits](output/pi-pi-1000000.txt.png)
