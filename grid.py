# Contains encoding for crossword grid
import pandas as pd
import numpy as np
import math

class Grid:

    MIN_WORD_LENGTH = 2


    def __init__(self, size, p=0.84):
        # How large to make the grid
        self.size = size
        # calculation taken from NYTXW max word guidelines
        self.max_words = math.ceil(4 + 0.312*size**2)
        # Initial probability of box being white
        self.p = p
        # generate random grid shape
        self.generate_grid()


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

    def generate_grid(self):
        # true if box is white, false if box is black
        self.grid = np.random.choice(a=[True, False], size=(self.size, self.size), p=[self.p, 1-self.p])
        self.enforce_symmetry()
        self.check_validity()


    def enforce_symmetry(self):
        # enforce rotational symmetry
        for i in range(self.size):
            rotated_i = self.size - 1 - i
            for j in range(self.size):
                rotated_j = self.size - 1 - j
                self.grid[rotated_i, rotated_j] = self.grid[i][j]
                
    
    # calculate grid stats
    def check_validity(self):
        valid = True
        # counting number of words
        self.word_count = 0
        for i in range(self.size):
            for j in range(self.size):
                if (not self.grid[i-1][j]) or (i == 0 and self.grid[i][j]):
                    self.word_count += 1
                if (not self.grid[i][j-1]) or (j == 0 and self.grid[i][j]):
                    self.word_count += 1

        # finding shortest word:
        # slice grid vertically and horizontally
        # find shortest substring of true values
        for row in self.grid:
            if not valid:
                break
            curr_word_length = 0
            for box in row:
                if box:
                    curr_word_length += 1
                else:
                    if curr_word_length < self.MIN_WORD_LENGTH:
                        # grid invalid
                        valid = False
                        break
        for j in range(self.size):
            col = self.grid[0:, j]
            if not valid:
                    break
            curr_word_length = 0
            for box in col:
                if box:
                    curr_word_length += 1
                else:
                    if curr_word_length < self.MIN_WORD_LENGTH:
                        # grid invalid
                        valid = False
                        break
        if not valid:
            self.generate_grid()

test_grid = Grid(6)
print(test_grid)


