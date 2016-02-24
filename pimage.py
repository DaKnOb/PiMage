#!bin/python

# Load Libraries
from PIL import Image
from random import randint

# Create New Image -- Black by default
img = Image.new( 'RGB', (255,255), "black")
pixels = img.load()

# Open file
pi = open("pi/100000.txt", "r")
piv = pi.read()
pi = pi.close()

# Remove 3. -- We want the decimals!
piv = piv[2:]

# Randomize all pixels
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (randint(0,255), randint(0,255), randint(0,255))

# Open the image
img.show()
