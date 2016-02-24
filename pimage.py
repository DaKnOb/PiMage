#!bin/python

from PIL import Image
from random import randint

img = Image.new( 'RGB', (255,255), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (randint(0,255), randint(0,255), randint(0,255))

img.show()
