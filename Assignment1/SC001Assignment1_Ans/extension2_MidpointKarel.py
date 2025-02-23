"""
File: extension2_MidpointKarel.py
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
    pre_condition: Karel is at Street1 Avenue1 facing East.
    post_condition: Karel is in the middle of Street1.
    """
    X_beeper()
    go_straight()
    I_beeper()
    pick_whole_beepers()



def X_beeper():
    """
    pre_condition: Karel is at Street1 Avenue1 facing East.
    post_condition: Karel is at Street5 Avenue5 facing
    """
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()
    turn_around()


def go_straight():
    while front_is_clear():
        move()
    turn_left()


def I_beeper():
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()
    turn_right()


def pick_whole_beepers():
    while front_is_clear():
        while facing_west():
            while front_is_clear():
                if on_beeper():
                    pick_beeper()
                    if front_is_clear():
                        move()
                    else:
                        turn_right()
                        if on_beeper():
                            pick_beeper()
                else:
                    move()
            turn_right()
            if on_beeper():
                pick_beeper()
        move()
        turn_right()

        while facing_east():
            while front_is_clear():
                if on_beeper():
                    pick_beeper()
                    if front_is_clear():
                        move()
                    else:
                        turn_left()
                        if on_beeper():
                            pick_beeper()
                else:
                    move()
            turn_left()
            if on_beeper():
                pick_beeper()
        move()
        turn_left()







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
