"""
File: complement.py
Name: Sidney
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    COMPLEMENT DNA A->T, T->A, G->C, C->G
    """
    dna = input('please give me a DNA strand and I\'ll find the complement:  ')
    new_dna = my_upper(dna)
    new_dna = sequence(new_dna)   # sequence(new_dna) change the ATGC
    print('The complement of ' + dna + ' is ' + new_dna)


def my_upper(dna):
    ans = ''
    for i in range(len(dna)):
        ch = dna[i]
        if ch.islower:
            ans += ch.upper()
        else:
            ans += ch
    return ans


def sequence(new_dna):
    ans = ''
    for i in range(len(new_dna)):
        ch = new_dna[i]
        if ch == 'A':
            ans = ans + 'T'
        elif ch == 'T':
            ans = ans + 'A'
        elif ch == 'G':
            ans = ans + 'C'
        elif ch == 'C':
            ans = ans + 'G'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
