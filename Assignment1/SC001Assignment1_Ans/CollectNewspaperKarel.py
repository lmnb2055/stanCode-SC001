"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at Street3 Avenue4 face west.
    post-condition: Karel is at Street3 Avenue4 face west and pick a beeper.
    """
    move_to_beeper()
    go_home()


def move_to_beeper():
    """
    pre-condition: Karel is at Street3 Avenue4 facing west
    post-condition: karel is at Street6 Avenue3 facing east with beepers
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_around()
    pick_beeper()


def go_home():
    """
    pre-condition: karel is at Street6 Avenue3 facing east with beepers
    post-condition: Karel is at Street3 Avenue4 facing west and put beepers
    """
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
