"""
File: similarity.py (extension)
Name: Sidney
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Homology: match a DNA sequence.
    """
    long_sequence: str = input('Please give me a DNA sequence to search:  ')
    long_sequence = long_sequence.upper()
    short_sequence = input('What DNA sequence would you like to match?  ')
    s = short_sequence.upper()
    f = match(s, long_sequence)
    dna = find_dna(s, long_sequence, f)   # according to f, finding the most match dna sequence.
    print('The best match' + dna)


def match(s, long_sequence):  # match short_sequence & long_sequence
    # calculate the number of short_sequence.

    # match long_sequence
    count1 = counting1(long_sequence)
    count2 = counting2(s)
    difference = count1 - count2
    add = 0
    most_match = 0.0
    while True:
        de = 0   # denominator
        num = 0  # numerator
        for i in range(len(s)):
            de += 1
            short = s[i]
            long = long_sequence[i+add]
            if short == long:
                num += 1
        value = float(num / de)
        if value > most_match:   # find the most match value
            most_match = value
        if add < difference:   # the variable 'add' helps to check the next sequence.
            add += 1
        else:
            break
    return most_match


def counting1(s):
    ans = 0
    for i in range(len(s)):
        ans += 1
    return ans


def counting2(long_sequence):
    ans = 0
    for i in range(len(long_sequence)):
        ans += 1
    return ans


def find_dna(s, long_sequence, f):
    count1 = counting1(long_sequence)
    count2 = counting2(s)
    difference = count1 - count2
    add = 0
    while True:
        de = 0  # denominator
        num = 0  # numerator
        for i in range(len(s)):
            de += 1
            short = s[i]
            long = long_sequence[i + add]
            if short == long:
                num += 1
        if float(num / de) == f:
            break
        if add < difference:
            add += 1
    ans = long_sequence[add:add+count2]
    return ans

















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
