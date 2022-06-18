from scipy.fftpack import dct
from image_processing import *
import cv2

stego_image = im("sloth.jpg")
#print(stego_image.Y)
print(len(stego_image.Y))
print(stego_image.Y[10000])
dct_blocks = [dct(block) for block in stego_image.Y]
print(len(dct_blocks))
print(dct_blocks[10000])

quantized_blocks = []
for n in dct_blocks:

    new_block = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            new_block[i][j] = int(float(n[i][j] * quant_table[i][j]))

    quantized_blocks.append(new_block)

print(quantized_blocks[10000])
