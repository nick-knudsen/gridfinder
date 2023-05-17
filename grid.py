# Contains encoding for crossword grid
import pandas as pd
import numpy as np
import math
import random

class Grid:

    def __init__(self):

        self.MIN_WORD_LENGTH = 3
        self.SIZE = 15
        self.CELL_PROB = 0.5

        # create empty grid
        self.grid = []
        # keep track of column depths
        self.depths = np.zeros(self.SIZE)
        # generate random grid shape
        self.generate_grid()


    def __str__(self):
            visual = ""
            for row in self.grid:
                for cell in row:
                    if cell:
                        visual += "| "
                    else:
                        visual += "|X"
                visual += "|\n"
            return visual

    def is_fully_connected(self):
        # visited = []
        # unvisited = [all white cells]
        # visit first unvisited cell
        # for cell in visited
            # visit all adjacent unvisited white cells
            # remove cell from visited
        # return len(unvisited) == 0
        pass

    def update_col_depths(self):
        top_row = self.grid[0]
        for cell, col_index in zip(top_row, range(self.SIZE)):
            if not cell:
                self.depths[col_index] = 0
                continue
            self.depths[col_index] += 1
        pass
    
    # generate a symmetric center row
    def generate_7th_row(self):
        width = 0
        row = np.zeros(self.SIZE)
        # for each col 0-6
        for col_index in range(7):
            # if width 1 or 2 cell must be white
            if width in (1,2):
                row[col_index] = 1
                width += 1
            else:
                # prob p cell white else black
                if random.random() > self.CELL_PROB:
                    row[col_index] = 1
                    width += 1
                    continue
                width = 0
                
        # center, col 7
        # if width = 1,2 cell must be white
        if width in (1,2):
            row[7] = 1
        if width > 2:
            # prob p cell white else black
            if random.random() > self.CELL_PROB:
                row[7] = 1
        # mirror cols 0-6 for cols 8-14
        row[14:7:-1] = row[0:7]
        return row

    def generate_6th_row(self):
        width = 0
        row = np.zeros(self.SIZE)

        for col_index in range(8):
            if self.depths[col_index] == 1:
                if col_index == 7:
                    # if center cell white, curr cell must be white
                    row[col_index] = 1
                    width += 1
                    self.depths[col_index] += 2
                    continue
                # if width 1 or 2 cell must be white
                if width in (1,2):
                    row[col_index] = 1
                    width += 1
                    self.depths[col_index] += 1
                    # mirrored cell can 'see through' middle row, increase depth
                    self.depths[self.SIZE-1-col_index] += 1
                    continue
            if random.random() > self.CELL_PROB:
                row[col_index] = 1
                self.depths[col_index] += 1
                continue
            width = 0
            self.depths[col_index] = 0
                    
        for col_index in range(8,15):
            if self.depths[col_index] == 1 or width in (1,2):
                # cell must be white
                row[col_index] = 1
                width += 1
                self.depths[col_index] += 1
        pass

    def generate_basic_row(self):
        # width 0
        # for each col
            # if depth or width 1 or 2 cell must be white
                # width += 1
            # else
                # cell black w/ prob p
                    # width 0
                # cell white w/ prob 1-p
                    # width += 1
        pass

    def generate_top_row(self):
        # width 0
        # for each col
            # if depth 0
                # cell black
                    # width 0
            # else if width 1,2
                # cell white
                    # width += 1
            # else
                # cell black w/ prob p
                    # width 0
                # cell white w/ prob 1-p
                    # width += 1
        pass

    def mirror_rows(self):
        # for row 0-6
            # row 14-row = row[::-1]
        pass

    # generate grids row-wise
    def generate_grid(self):
        row_7 = self.generate_7th_row()
        self.grid.insert(0, row_7)
        self.update_col_depths()
        # update column depths
        # generate valid row 6
        # for rows 5-3:
            # generate valid row
            # update column depths
        # row 2
        # generate valid row 
        # find num components
        # while not is_fully_connected()
            # generate valid row
        # update column depths
        # for rows 1,0:
            # generate valid top row
            # update column depths
        # mirror rows 0-6 to rows 14-8
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


