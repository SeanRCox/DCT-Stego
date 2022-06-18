from PIL import Image
import numpy as np

quant_table = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                       [12, 12, 14, 19, 26, 58, 60, 55],
                       [14, 13, 16, 24, 40, 57, 69, 56],
                       [14, 17, 22, 29, 51, 87, 80, 62],
                       [18, 22, 37, 56, 68, 109, 103, 77],
                       [24, 36, 55, 64, 81, 104, 113, 92],
                       [49, 64, 78, 87, 103, 121, 120, 101],
                       [72, 92, 95, 98, 112, 100, 103, 99]])

class im :
    def __init__(self, image) :
        img = get_image_data(image) #getting image data
        if img.shape[0] % 8 != 0 or img.shape[1] % 8 != 0 : #resizing image if need be
            resize_image(img)
        #img = RGBtoYCbCr(img) #converting image from RGB to YCbCr

        #creating 8x8 blocks for Luminance, Chroma Blue, Chroma Red
        self.Y = create_blocks(img[:,:,0]) 
        self.Cb = create_blocks(img[:,:,1])
        self.Cr = create_blocks(img[:,:,2])

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
    image = Image.open(file)
    return np.asarray(image)

def create_blocks(image) : #turn the image into 8x8 blocks of the RGB values
    blocks = []
    for vert_slice in np.vsplit(image, int(image.shape[0] / 8)):
        for horiz_slice in np.hsplit(vert_slice, int(image.shape[1] / 8)):
            blocks.append(horiz_slice)
    return blocks

def RGBtoYCbCr(im) :
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return np.uint8(ycbcr)

