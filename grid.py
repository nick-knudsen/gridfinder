# Contains encoding for crossword grid
import pandas as pd
import numpy as np

class Grid:
    def __init__(self, size):
        # How large to make the grid
        self.size = size

        # Initial probability of box being white
        P = 0.84

        #Grid Rules
        MAX_WORDS = 30
        MIN_WORD_LENGTH = 3

        # Contains grid shape
        # true if box is white, false if box is black
        self.grid = np.random.choice(a=[True, False], size=(self.size, self.size), p=[P, 1-P])

    def __str__(self):
        for box in self.grid:
            print("O") if box else print("X")
    
    # calculate grid stats

    # counting number of words in a crossword grid:
    #   if a box above or left of a given box is black (false), current box
    #   is the first letter of a new word

    # finding shortest word:
    # slice grid vertically and horizontally
    # find shortest substring of true values




