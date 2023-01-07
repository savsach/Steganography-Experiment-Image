from PIL import Image
import numpy as np
import argparse

MAX_MSG_LENGTH= 500
parser = argparse.ArgumentParser(description = 'decrypt messages from image')
parser.add_argument('-i', '--image', required=True)
args = parser.parse_args()

img=np.array(Image.open(args.image))

rowLength = len(img)
colLength= len(img[0])
byteList = []

# Creating bytes using LSB of every pixel
j = 0
decrypting = True
while (decrypting):
    add = 128
    byte = 0
    for i in range(8):
        row = int((i+j)/colLength)
        if (row >= rowLength):
            decrypting=  False
            break
        if ((img[row][(i+j)%colLength][2] % 2)): 
            byte+= add
        add/= 2    
    byteList.append(int(byte))
    j+=8


msg= bytearray(byteList)
ret_str = msg.decode('utf-8', 'ignore')
print(ret_str[0:MAX_MSG_LENGTH])
