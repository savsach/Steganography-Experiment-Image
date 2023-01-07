from PIL import Image
import numpy as np
import bitstring
import sys
import matplotlib.image
import argparse

parser = argparse.ArgumentParser(description = 'encrypt messages to image')
parser.add_argument('-i', '--image', required=True)
parser.add_argument('-t', '--text', required=True)
args = parser.parse_args()

img=np.array(Image.open(args.image))
str_enc = bytes(args.text,'UTF-8')
bitArr = bitstring.Bits(bytes=str_enc)

rowLength = len(img)
colLength= len(img[0])
for index in range(len(bitArr)):
    if (index > rowLength*colLength):
        print("Message too long to be encrypted in current image")
        sys.exit(1)
    row = int(index/colLength)    
    if (bitArr[index] != img[row][index%colLength][2] %2):
        if (img[row][index%colLength][2] <128):
            img[row][index%colLength][2] += 1
        else:
            img[row][index%colLength][2] -= 1  

matplotlib.image.imsave('ret.png', img)
