"""
File: MidpointKarel.py
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
    pre-condition: Karel is at S1 A1 facing East.
    post-condition: Karel is at the middle of the Street 1.
    """
    wall_beepers()
    while not on_beeper():
        according_to_beepers()
    turn_around()
    pick_beeper()
    move()


def wall_beepers():
    """
    pre_condition: Karel is at S1 A1 facing East.
    post_condition: Karel put the beepers on left and right side and at S1 A4 facing west.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()


def turn_around():
    turn_left()
    turn_left()


def according_to_beepers():
    """
    found the left side beeper and take them to the middle.
    """
    while not on_beeper():
        move()
    pick_beeper()
    turn_around()
    move()
    put_beeper()
    move()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
