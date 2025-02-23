"""
File: hangman.py
Name: Sidney
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Randomly choose the answer, which will be showed with dashes.
    The words would be dashed at first.
    """
    answer = random_word()
    d = dashes(answer)   # calculate the dashes from random words.
    print('The word looks like ' + d)
    le = 7   # user's lives
    print('You have 7 wrong guesses left.')
    while True:
        if not d.isalpha():
            if le != 0:       # can play the game
                guess = str(input('Your guess: '))
                guess = guess.upper()   # upper alphabets
                if not guess.isalpha():
                    # if there are other types except for alphabets, it shows "illegal format."
                    print('Illegal format.')
                else:
                    if answer.find(guess) == -1:
                        print('There is no ' + guess + "'s in the word.")
                        le -= 1
                        print('You have ' + str(le) + ' wrong guesses left.')
                    else:
                        print('You are correct!')
                        d = replace(answer, d, guess)
                        if not d.isalpha():
                            print('The word looks like ' + str(d))
            else:
                print('You are completely hung : ( \nThe word was: ' + str(answer))
                break
        else:
            print('You Win!\nThe word is ' + str(answer))
            break


def replace(answer, d, guess):
    current_word = ''
    for i in range(len(answer)):
        ch = answer[i]
        if guess == answer[i]:
            current_word += guess
        else:
            if d[i].isalpha():
                current_word += ch
            else:
                current_word += '-'
    return current_word


def dashes(answer):
    s = answer
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if ch.isalpha():
            ans += '-'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
