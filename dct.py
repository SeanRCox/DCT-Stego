import cv2 as cv2 #for dct calculation

from image_processing import *
from zig_zag import zig_zag

stego_image = im("images/cat.jpg")
print((stego_image.layers[0])[1000])
dct_blocks = [np.uint8(cv2.dct(np.float32(block)/255.0) * 255) for block in stego_image.layers[0]]
print(dct_blocks[1000])

quantized_blocks = []
for n in dct_blocks:

    new_block = np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            new_block[i][j] = int(n[i][j] / quant_table[i][j])

    quantized_blocks.append(new_block)

print(quantized_blocks[1000])

print(zig_zag(quantized_blocks[1000]))
