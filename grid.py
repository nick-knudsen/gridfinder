# Contains encoding for crossword grid
import pandas as pd
import numpy as np
import math

class Grid:

    MIN_WORD_LENGTH = 3
    SIZE = 15

    def __init__(self):
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

    def find_connected_component(self):
        pass

    def update_col_depths(self):
        # for each col
            # if top white depth += 1
            # else depth 0
        pass
    
    def generate_0th_row(self):
        # must be symmetric
        pass

    def generate_1st_row(self):
        # width 0
        # for each col 0-8
            # if depth 1
                # if center, cell must be white
                    # width += 1
                    # depth += 2
                # if width 1 or 2 cell must be white
                    # width += 1
                    # depth += 1
                    # depth_n-col+1 += 1
                # else
                    # w/ prob p cell black
                        # width = 0
                        # depth = 0
                    # w/ prob 1-p cell white
                        # width += 1
                        # depth += 1
                        # depth_n-col+1 += 1
            # if depth 0
                # if width 1 or 2 cell must be white
                    # width += 1
                    # depth += 1
                # else
                    # w/ prob p cell black
                        # width = 0
            

        pass

    def generate_basic_row(self):
        # width 0
        # for each col
            # if depth or width 1 or 2 cell must be white
                # width += 1
            # otherwise cell may be black w/ prob p?
                # width 0
        pass
    
    def generate_5th_row(self):
        pass

    # generate grids row-wise
    def generate_grid(self):
        # generate random row 0
        # update column depths
        # generate valid row 1
        # update column depths
        # for rows 2-4:
            # generate valid row
            # update column depths
        # generate valid row 5
        # for rows 6,7:
            # generate valid row
        pass

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
            curr_word_length = None
            for box in row:
                if box and curr_word_length is None:
                    curr_word_length = 1
                elif box:
                    curr_word_length += 1
                elif not box and curr_word_length is None:
                    pass
                else:
                    if curr_word_length < self.MIN_WORD_LENGTH:
                        # grid invalid
                        valid = False
                        break
        for j in range(self.size):
            col = self.grid[0:, j]
            if not valid:
                    break
            curr_word_length = None
            for box in col:
                if box and curr_word_length is None:
                    curr_word_length = 1
                elif box:
                    curr_word_length += 1
                elif not box and curr_word_length is None:
                    pass
                else:
                    if curr_word_length < self.MIN_WORD_LENGTH:
                        # grid invalid
                        valid = False
                        break
        return valid

test_grid = Grid()
print(test_grid)


