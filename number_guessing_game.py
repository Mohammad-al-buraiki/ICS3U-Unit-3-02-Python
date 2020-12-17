#!/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is Number Guessing Game

import constants


def main():
    # this function asks the user to guess the right number

    # input
    guessing = int(input("Guess the right number between 1-10: "))
    print("")

    # process
    if guessing == constants.GUESSIN_NUMBER:
        # output
        print("You got it right")


if __name__ == "__main__":
    main()
