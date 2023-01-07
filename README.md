# Steganography-Experiment-Image
A trivial way to encode messages in Images

Dependencies
--------------------
1) python3
1) matplotlib
1) PIL
1) numpy
1) bitstring

Usage
---------------------
Use the encryption script to create an image with your message encoded in it
```
python3  encrypt.py -i <image-file> -t <text-message>
```
Use the decryption script to print out the encrypted message in your image
```
python3  decrypt.py -i <encrypted-image-file> 
```
