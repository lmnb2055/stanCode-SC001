"""
File: caesar.py
Name: Sidney
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program is going to decipher. There is a secret number to decide how many alphabets should be moved.
    Having the secret number and ciphered string, we could know the deciphered string.
    """
    n = int(input('Secret number: '))
    s = input("What's the ciphered string? ")
    new = new_alphabet(n)  # move the original alphabet
    s = s.upper()   # upper all alphabet from users
    print('The deciphered string is: ', end='')    # The deciphered string is ANSWER.
    for i in range(len(s)):
        ch = s[i]
        if s[i].isalpha():
            a = new.find(ch)
            ciphered = ALPHABET[a]
            print(ciphered, end='')   # parts of ANSWER
        else:
            print(ch, end='')   # parts of ANSWER


def new_alphabet(n):
    ans = ''
    front = ALPHABET[(26-n):]
    back = ALPHABET[:(26-n)]
    ans = front + back
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
