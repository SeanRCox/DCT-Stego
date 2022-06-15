from PIL import Image
import numpy as np

def resize_image(img):
    # takes an image and resizes it if not multiple of 8
    # returns 1 if it resized
    im = Image.open(img)
    width, height = im.size
    if (closest_factor(width,8) != width | closest_factor(height,8) != height) :
        im = im.resize((closest_factor(width,8), closest_factor(height,8)))
        im.save(img)
        return 1
    return 0

def closest_factor(num, fac): #Function for finding closest value that is a factor, used for resize on w and h
    for i in range(fac):
        if (num + i) % fac == 0:
            num += i
            break
        elif (num - i) % fac == 0:
            num -= i
            break
    print(num)
    return num

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

