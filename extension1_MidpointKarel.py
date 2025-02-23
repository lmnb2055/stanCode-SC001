"""
File: extension1_MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre_condition: Karel is at S1 A1 facing east and no beepers.

    put beepers in the middle except for the place next to the wall.

    post_condition: Karel is at S1 A5 facing west and no beepers.

    """
    beepers_in_the_middle()
    while on_beeper():
        pick_whole_beepers()
    middle()


def beepers_in_the_middle():
    move()
    while front_is_clear():
        put_beeper()
        move()
    turn_around()
    move()


def turn_around():
    turn_left()
    turn_left()


def pick_whole_beepers():
    while on_beeper():
        move()
    turn_around()
    move()
    pick_beeper()
    move()


def middle():
    turn_around()
    move()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
