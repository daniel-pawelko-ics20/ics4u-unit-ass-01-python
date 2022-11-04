#!/usr/bin/env python3

# Created on: Nov-2022
# Created by: Daniel Pawelko
# Created for: ICS4U
# Rock Paper Scissors

# Imports
from numpy import isnan, nan
from random import random
from math import floor


def main():
    # Define variables
    LOGIC = [
        [1, 3],  # rock > sicssors
        [2, 1],  # paper > scissors
        [3, 2],  # scissors > paper
    ]
    NUM_TO_WORD = ["Rock", "Paper", "Scissors"]

    selection_up = ""
    selection = 0

    while isnan(selection) or selection <= 0 or selection >= 4:
        # This is not a good way of writing it but I wanted to make it as
        # similar to the typescript version as there is also a flowchart to
        # follow(kinda)
        try:
            selection_up = input("[1] Rock, [2] Paper, [3] Scissors: ")
            selection = int(selection_up)
        except:
            selection = nan

    random_num = floor(random() * 3) + 1

    for selection_loop in range(len(LOGIC)):
        if selection == random_num:
            # If user input and computer is the same than it is a tie
            print("Tie :|")
            break
        elif selection in LOGIC[selection_loop] and random_num in LOGIC[selection_loop]:
            if LOGIC[selection_loop][0] == selection:
                print(
                    f"You won! {NUM_TO_WORD[selection - 1]} beats {NUM_TO_WORD[random_num - 1]}"
                )
            else:
                print(
                    f"You Lost :( {NUM_TO_WORD[random_num - 1]} beats {NUM_TO_WORD[selection - 1]}"
                )

    # Done
    print("\nDone.")


if __name__ == "__main__":
    main()
