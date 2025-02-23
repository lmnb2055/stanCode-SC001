"""
File: rocket.py
Name: Sidney
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    print strings -> head, belt, upper, lower, belt, head -> look like a rocket.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):    # print ''
            print(' ', end='')
        for j in range(i+1):       # print'/'
            print('/', end='')
        for j in range(i+1):       # print'\'
            print('\\', end='')
        print('')


def belt():
    print('+', end='')        # + in the left side
    for i in range(SIZE*2):
        print('=', end='')    # -------------
    print('+')                # + in the right side


def upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-i-1):   # print .. . (i = 2, 1 , 0)
            print('.', end='')
        for j in range(i+1):
            print('/', end='')      # print /\  (i = 1, 2, 3)
            print('\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')     # print .. . (i = 2, 1 , 0)
        print('|')


def lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')     # print  . .. (i = 0, 1 , 2)
        for j in range(SIZE-i):
            print('\\', end='')
            print('/', end='')     # print \/ (i = 3, 2, 1)
        for j in range(i):
            print('.', end='')     # print  . .. (i = 0, 1 , 2)
        print('|')








# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
