"""
File: fire.py
Name:Sidney
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image (with respect to current directory)
    :return: gray_scale picture with sign the fire region
    """
    gray_img = SimpleImage(filename)
    for pixel in gray_img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:   # strong fire pixel, emphasize on red pixel
            pixel.red = 225
            pixel.green = 0
            pixel.blue = 0
        else:   # gray scale
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return gray_img


def main():
    """
    This file contains a image processing algorithms:
    gray_scale picture with sign the fire region
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
