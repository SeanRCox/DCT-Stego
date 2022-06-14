from scipy.fftpack import dct
from image_processing import *

img = get_image_data("sloth.jpg")
data = create_blocks(img)
print(len(data))
print(data[0])
print(dct(data[0]))