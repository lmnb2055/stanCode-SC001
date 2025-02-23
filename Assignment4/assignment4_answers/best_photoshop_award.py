"""
File: best_photoshop_award.py
Name:Sidney
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def main():
    """
    創作理念：身為淺淺的marvel fans，每次進到電影院看系列電影時，總還是能被鋼鐵人和蜘蛛人給帥到，覺得他們超酷超炫，
            所以這次我也想化身成為Spider Man, 在城市天際中跳來跳去，來達成小小的英雄夢XD
    """
    fig = SimpleImage('image_contest/fly.jpg')
    bg = SimpleImage('image_contest/city.jpeg')
    bg.make_as_big_as(fig)
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.blue + fig_pixel.green) // 3
            if avg > 195:
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
