"""
File: name_sq.py (extension)
Name: Sidney
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    This program prints a name in a square pattern!
    """
    print('This program prints a name in a square pattern!')
    name = input('Name: ')  # input a name
    c = count(name)  # count alphabets
    rev = reverse(name)  # reverse the name
    print(name)
    squ = square(name, c, rev)  # the function helps to print left and right sides.
    print(squ, end="")  # print the square.
    print(rev)


def square(name, c, rev):
    # calculate the space
    space = ""
    for i in range(c-2):
        space += " "
    ans = ''
    #  arrange the first col and last col.
    for i in range(1, c-1):  # alphabets except the first and last one.
        for j in range(1):
            ch = name[i]
            ch1 = rev[i]
            ans = ans + ch + space + ch1 + '\n'  # change line.
    return ans


def count(name):
    c = 0
    for i in range(len(name)):
        c += 1
    return c


def reverse(name):
    result = ''
    for i in range(len(name)):
        result = name[i] + result
    return result

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
