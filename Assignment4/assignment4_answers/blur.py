"""
File: blur.py
Name:sidney
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):


            # Todo: get pixel of new_img at x,y
            pixel = new_img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            # if x == 0 and y ==0:
            new_r = 0
            new_g = 0
            new_b = 0
            if x == 0 and y == 0:
                for i in range(0, 2):
                    for j in range(0, 2):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 4
                pixel.green = new_g // 4
                pixel.blue = new_b // 4


            # Get pixel at the top-left corner of the image.


            # elif ...:
            #Get pixel at the bottom-left corner of the image
            elif x == 0 and y == new_img.height-1:
                for i in range(0, 2):
                    for j in range(new_img.height-2, new_img.height):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 4
                pixel.green = new_g // 4
                pixel.blue = new_b // 4
            # elif ...:
            # Get pixel at the top-right corner of the image.
            elif x == new_img.height-1 and y == 0:
                for i in range(new_img.width-2, new_img.width):
                    for j in range(0, 2):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 4
                pixel.green = new_g // 4
                pixel.blue = new_b // 4
            # elif ...:
            # Get pixel at the bottom-right corner of the image
            elif x == new_img.width-1 and y == new_img.height-1:
                for i in range(new_img.width-2, new_img.width):
                    for j in range(new_img.height-2, new_img.height):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 4
                pixel.green = new_g // 4
                pixel.blue = new_b // 4
            # elif ...:
            # Get top edge's pixels (without two corners)
            elif y == 0:
                for i in range(x-1, x+2):
                    for j in range(y, y+2):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 6
                pixel.green = new_g // 6
                pixel.blue = new_b // 6
            # elif ...:
            # Get bottom edge's pixels (without two corners)
            elif y == new_img.height-1:
                for i in range(x-1, x+2):
                    for j in range(new_img.height-2, new_img.height):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 6
                pixel.green = new_g // 6
                pixel.blue = new_b // 6
            # elif ...:
            # Get left edge's pixels (without two corners)
            elif x == 0:
                for i in range(x, x+2):
                    for j in range(y-1, y+2):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 6
                pixel.green = new_g // 6
                pixel.blue = new_b // 6
            # elif ...:
            # Get right edge's pixels (without two corners)
            elif x == new_img.width-1:
                for i in range(new_img.width-2, new_img.width):
                    for j in range(y-1, y+2):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 6
                pixel.green = new_g // 6
                pixel.blue = new_b // 6
            # else:
            else:
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        new_r += img.get_pixel(i, j).red
                        new_g += img.get_pixel(i, j).green
                        new_b += img.get_pixel(i, j).blue
                pixel.red = new_r // 9
                pixel.green = new_g // 9
                pixel.blue = new_b // 9

            # Inner pixels.

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
