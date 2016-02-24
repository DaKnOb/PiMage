#!bin/python

# Load Libraries
from PIL import Image
from random import randint
from math import sqrt

PI_DIGITS_FILE = "pi/100000.txt"

# Open file
pi = open(PI_DIGITS_FILE, "r")
piv = pi.read()
pi = pi.close()

# Remove 3. -- We want the decimals!
piv = piv[2:]

# Calculate Image Dimensions
pilen = len(piv)
pilen = sqrt(pilen)
pilen = int(pilen)

# Create New Image -- Black by default
img = Image.new( 'RGB', (pilen, pilen), "red")
pixels = img.load()

# Run through the entire Pi and calculate RGB values
for i in xrange(0,pilen*pilen):
	Color = int(int(piv[i]) * 20) 
	pixels[i % pilen, int( i / pilen )] = (Color, Color, Color)

# Open the image
img.show()
img.save("output/pi-" + PI_DIGITS_FILE.replace("/", "-") + ".png")
