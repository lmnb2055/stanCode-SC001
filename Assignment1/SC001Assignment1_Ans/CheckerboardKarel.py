"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:
    Karel is at Street 1 Avenue 1 facing East
    post-condition:
    a wall is in the north, finish the checkerboard no matter where is Karel

    """

    while not facing_north():
        fill_one_line()
        jump()
        if not facing_north():
            fill_second_line()



def fill_one_line():
    """
    pre-conditiion:  Karel faces East and must put a beeper on Avenue 1.
    post-condition:  karel is at Avenue 8 facing north.

    """
    put_beeper()
    while front_is_clear():
        if on_beeper():
            move()
        if front_is_clear():
            move()
            put_beeper()
    pass
    turn_left()


def jump():
    """
    pre-condtion: karel is at Street 1 Avenue 8 facing north.
    post-condition: karel is at Street 2 Avenue 8 facing west and decide to whether to put beeper or not.
    """
    if front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
            turn_left()
        else:
            move()
            turn_left()




def fill_second_line():
    """
    pre-condition: karel is at Street 2 Avenue 8 facing west.
    post-condition: karel is at Street 2 Avenue 1 facing north.

    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            move()
            put_beeper()
    pass
    turn_right()
    if front_is_clear():
        move()
        turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()













# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
