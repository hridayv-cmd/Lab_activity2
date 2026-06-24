"""
Program Name: coin.py
Author: Hriday Vermani
Purpose: Represents a single, tossable coin with a private state of either 'Heads' or 'Tails'.
Starter Code: None
Date: June 24 2026
"""
import random

class Coin:
    def __init__(self):
        """Initializes the coin and determines its initial side up."""
        self.__sideup = 'Heads'
        self.toss()  # Automatically toss to randomize the initial state
    def toss(self):
        """Generates a random choice and sets __sideup to 'Heads' or 'Tails'."""
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        """Returns the current value of __sideup."""
        return self.__sideup