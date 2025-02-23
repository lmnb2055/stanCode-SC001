"""
File: extension2_number_checker.py
Name: Sidney
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

Exit = -100

def main():
    """
    number checker: perfect number, abundant number, deficient number
    """
    print('Welcome to the number checker!')
    while True:
        n = int(input('n: '))
        # variable m  help us to minus n.
        m = n
        if n == Exit:
            print('Have a good one! ')
            break
        else:
            # check the number 1 to n-1, which can be factors of n.
            for i in range(1, n):
                if n % i == 0:
                    m += i
            # all factors except for itself
            m -= n

        if m == n:
            print(str(n) + ' is a perfect number.')
        elif m > n:
            print(str(n) + ' is a abundant number.')
        else:
            print(str(n) + ' is a deficient number.')





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
