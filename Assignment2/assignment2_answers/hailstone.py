"""
File: hailstone.py
Name: Sidney
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    print('This program computes Hailstone sequences.')
    num = int(input('Enter a number: '))
    step = 0
    while True:
        if num == 1:
            break
        elif num % 2 == 0:
            new = num // 2
            print(str(num) + ' is even, so I take half: ' + str(new))
            num = new
        else:
            new1 = num * 3
            new1 += 1
            print(str(num) + ' is even, so I make 3n+1: ' + str(new1))
            num = new1
        step += 1
    print('It took ' + str(step) + ' steps to reach 1.')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
