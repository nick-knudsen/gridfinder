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
        self.enforce_symmetry()


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


    def enforce_symmetry(self):
        # enforce rotational symmetry
        for i in range(self.size):
            rotated_i = self.size - 1 - i
            for j in range(self.size):
                rotated_j = self.size - 1 - j
                self.grid[rotated_i, rotated_j] = self.grid[i][j]
                

    
    # calculate grid stats
    def calc_stats(self):
        # counting number of words
        word_count = 0
        for i in range(self.size):
            for j in range(self.size):
                if (not self.grid[i-1][j]) or (i == 0 and self.grid[i][j]):
                    word_count += 1
                if (not self.grid[i][j-1]) or (j == 0 and self.grid[i][j]):
                    word_count += 1
        print(word_count)
        # finding shortest word:
        # slice grid vertically and horizontally
        # find shortest substring of true values

test_grid = Grid(5)
print(test_grid)
test_grid.calc_stats()


