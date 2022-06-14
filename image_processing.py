from PIL import Image
import numpy as np

def get_image_data(file) : # opens image and returns the RGB data as a numpy array
    image = Image.open('sloth.jpg')
    return np.asarray(image)

def create_blocks(image) : #turn the image into 8x8 blocks of the RGB values
    blocks = []
    for vert_slice in np.vsplit(image, int(image.shape[0] / 8)):
        for horiz_slice in np.hsplit(vert_slice, int(image.shape[1] / 8)):
            blocks.append(horiz_slice)
    return blocks

def make_array(blocks) : # puts the 8x8 blocks into an array so the DCT coefficents can be calculated
    pass
