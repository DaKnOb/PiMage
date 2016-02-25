# PiMage
Pi, as an Image

PiMage is a Python utility that will read an arbitralily long text file containing
Pi to as many decimal digits as possible and then will generate an image where each
pixel is colored based on its digits.

## How are colors calculated:
Each pixel is either colored in a shade of Red, Green, or Blue in sequential order.
That means the first pixel is colored in a shade of Red, the second in a shade of Green,
the third in a shade of Blue, etc. The shade of the color is determined by a single digit
of pi multiplied by 28. That means the first digit, which is 1, it will be colored with
`(28,0,0)`, the second digit, a 4, will be colored with `(0,112,0)`, and the third digit,
which is again an 1, will be colored with `(0,0,28)`.

## Example Outputs
The first 100,000 digits of Pi:

![100k Pi Digits](output/pi-pi-100000.txt.png)

The first 1,000,000 digits of Pi:

![1M Pi Digits](output/pi-pi-1000000.txt.png)
