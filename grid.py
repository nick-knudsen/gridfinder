# Contains encoding for crossword grid
import pandas as pd
import numpy as np
import math

class Grid:

    MIN_WORD_LENGTH = 3

    def __init__(self, size, p=0.84):
        # How large to make the grid
        self.size = size
        # calculation taken from NYTXW max word guidelines
        self.max_words = math.ceil(4 + 0.312*size**2)
        # Initial probability of box being white
        self.p = p

        # generate random grid shape
        # true if box is white, false if box is black
        self.grid = np.random.choice(a=[True, False], size=(self.size, self.size), p=[p, 1-p])
        self.__enforce_symmetry__()

    def __enforce_symmetry__(self):
        # enforce rotational symmetry
        for i in range(self.size):
            rotated_i = self.size - 1 - i
            for j in range(self.size):
                rotated_j = self.size - 1 - j
                self.grid[rotated_i, rotated_j] = self.grid[i][j]
                

    def __str__(self):
        visual = ""
        for row in self.grid:
            for box in row:
                if box:
                    visual += "| "
                else:
                    visual += "|X"
            visual += "|\n"
        return visual
    # calculate grid stats

    # counting number of words in a crossword grid:
    #   if a box above or left of a given box is black (false), current box
    #   is the first letter of a new word

    # finding shortest word:
    # slice grid vertically and horizontally
    # find shortest substring of true values

test_grid = Grid(15)
print(test_grid)


