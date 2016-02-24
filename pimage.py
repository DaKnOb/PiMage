#!bin/python

# Load Libraries
from PIL import Image
from random import randint
from math import sqrt

PI_DIGITS_FILE = "pi/1000000.txt"

# Open file
pi = open(PI_DIGITS_FILE, "r")
piv = pi.read()
pi = pi.close()

# Remove 3. -- We want the decimals!
piv = piv[2:]

# Calculate Image Dimensions
pilen = len(piv)
pilen = int(pilen/9)
pilen = sqrt(pilen)
pilen = int(pilen)

# Create New Image -- Black by default
img = Image.new( 'RGB', (pilen, pilen), "black")
pixels = img.load()

# Run through the entire Pi and calculate RGB values
for i in xrange(0,(pilen*pilen*9),9):
	red = piv[i:i+3]
	green = piv[i+3:i+6]
	blue = piv[i+6:i+9]
	red = int(red) % 256
	green = int(green) % 256
	blue = int(blue) % 256
	# Add color to the image
	pixels[(i / 9) % pilen, int(i / 9 / pilen)] = (red, green, blue)

# Open the image
img.show()
img.save("output/pi-" + PI_DIGITS_FILE.replace("/", "-") + ".png")
