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
img = Image.new( 'RGB', (pilen, pilen), "black")
pixels = img.load()

# Randomize all pixels
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (randint(0,255), randint(0,255), randint(0,255))

# Open the image
img.show()
