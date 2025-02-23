"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at Street1 Avenue1 facing east.
    post-condition: Karel is at the left side of Street1 facing east.
    """
    while front_is_clear():
        fix_pillar()
        turn_to_origin()
        move_to_next_pillar()
    fix_pillar()
    turn_to_origin()


def fix_pillar():
    """
    pre-condition: Karel is at Street1 Avenue1 facing east.
    post-condition: Karel is at Street5 Avenue1 facing north.
    """
    turn_left()
    for i in range(4):
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    while not on_beeper():
        put_beeper()
    pass


def turn_to_origin():
    turn_around()
    for i in range(4):
        move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_to_next_pillar():
    move()
    move()
    move()
    move()





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
