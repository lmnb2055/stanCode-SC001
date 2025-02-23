"""
File: extension3_triangular_checker.py
Name:Sidney
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

Exit = -100

def main():
    """
    triangular number checker: the right data should be add from 1 to n...
    """
    print('Welcome to the triangular number checker!')
    while True:
        # give a triangular number.
        tn = int(input('tn: '))
        # n can be applied in calculation.
        n = 0
        # finish the project.
        if tn == Exit:
            print('Have a good one! ')
            break
        else:
            while True:
                # tn = n(n+1)/2
                a = n * (n+1)
                a /= 2
                # if a is smaller, n adds 1 and  a  keeps doing calculation.
                if a <= tn:
                    break
                else:
                    n += 1
        if tn == a:
            print(str(tn) + ' is a triangular number')
        # if a is bigger than tn, it means they are not equal.
        if tn < a:
            print(str(tn) + ' is not a triangular number')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
