# Contains encoding for crossword grid
import pandas as pd
import numpy as np
import math
import random

class Grid:

    def __init__(self):

        self.MIN_WORD_LENGTH = 3
        self.SIZE = 15
        self.CELL_PROB = 0.25

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
                        visual += "|X"
                    else:
                        visual += "| "
                visual += "|\n"
            return visual

    # TODO: method for conditional prob based cell fill method
    #       pass in cell indices, will need prob map
    #       call from anywhere cell is randomly filled

    def is_fully_connected(self):
        visited_cells = []
        cell_status = np.full((len(self.grid),self.SIZE), False)

        # visit first unvisited cell
        break_next = False
        for i in range(len(self.grid)):
            if break_next:
                break
            for j in range(len(self.grid[i])):
                if self.grid[i][j]:
                    visited_cells.append((i,j))
                    cell_status[i][j] = True
                    break_next = True
                    break
        
        # visit all connected cells
        while visited_cells:
            cell = visited_cells[0]
            row = cell[0]
            col = cell[1]
            # check all adjacent cells
            for adj_row, adj_col in zip((-1,0,0,1), (0,-1,1,0)):
                new_row = row+adj_row
                new_col = col+adj_col
                # check for valid index
                if new_row < 0 or new_row > len(self.grid)-1 or new_col < 0 or new_col > len(self.grid[0])-1:
                    continue
                # if cell is white and unvisited, visit it
                if self.grid[new_row][new_col] and not cell_status[new_row][new_col]:
                    cell_status[new_row][new_col] = True
                    visited_cells.append((new_row, new_col))
            
            visited_cells.pop(0)

        # compare visited cells and white cells, will be the same in a fully connected grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] and not cell_status[i][j]:
                    return False
        return True

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
        
        for col_index in range(7):
            if width in (1,2):
                # width 1 or 2 cell must be white
                row[col_index] = 1
                width += 1
                continue
            # cell can be black or white
            if random.random() > self.CELL_PROB:
                row[col_index] = 1
                width += 1
                continue
            width = 0
                
        # center, col 7
        if width in (1,2):
            # width 1 or 2, cell must be white
            row[7] = 1
        if width > 2:
            # cell can be black or white
            if random.random() > self.CELL_PROB:
                row[7] = 1
        # mirror cols 0-6 for cols 8-14
        row[14:7:-1] = row[0:7]
        return row

    def generate_6th_row(self):
        width = 0
        row = np.zeros(self.SIZE)

        for col_index in range(8):
            if self.depths[col_index] == 1 and col_index == 7:
                # center cell white, curr cell must be white
                row[col_index] = 1
                width += 1
                self.depths[col_index] += 2
                continue
            if width in (1,2):
                # width 1 or 2, cell must be white
                row[col_index] = 1
                width += 1
                self.depths[col_index] += 1
                if self.depths[col_index] == 2:
                    # mirrored cell can 'see through' middle row, increase depth
                    self.depths[self.SIZE-1-col_index] += 1
                continue
            # cell can be black or white
            if random.random() > self.CELL_PROB:
                row[col_index] = 1
                width += 1
                self.depths[col_index] += 1
                continue
            width = 0
            self.depths[col_index] = 0
                    
        for col_index in range(8,15):
            if col_index in (13,14) and width == 0:
                # last two cells must be black when previous one is
                self.depths[col_index] = 0
                continue
            if self.depths[col_index] == 1 or width in (1,2):
                # width 1 or 2, cell must be white
                row[col_index] = 1
                width += 1
                self.depths[col_index] += 1
                continue
            # cell can be black or white
            if random.random() > self.CELL_PROB:
                row[col_index] = 1
                width += 1
                self.depths[col_index] += 1
                if self.depths[col_index] == 2:
                    # mirrored cell can 'see through' middle row, increase depth
                    self.depths[self.SIZE-1-col_index] += 1
                continue
            width = 0
            self.depths[col_index] = 0
        return row

    def generate_basic_row(self):
        width = 0
        row = np.zeros(self.SIZE)

        for col_index in range(self.SIZE):
            if col_index in (13,14) and width == 0:
                continue
            if self.depths[col_index] in (1,2):
                row[col_index] = 1
                width += 1
                continue
            if width in (1,2):
                row[col_index] = 1
                width += 1
                continue
            if random.random() > self.CELL_PROB:
                row[col_index] = 1
                width += 1
                continue
            width = 0
        return row

    def generate_top_row(self):
        width = 0
        row = np.zeros(self.SIZE)

        # turn all legal cells white
        for col_index in range(self.SIZE):
            if self.depths[col_index] == 0:
                if width in (1,2):
                    # too narrow for previous white cells
                    row[col_index-2] = 0
                    row[col_index-1] = 0
                width = 0
                continue
            row[col_index] = 1
            width += 1
        return row

    def mirror_rows(self):
        bottom_half = [[False]*15]*7
        for row in range(7):
            bottom_half[6-row] = self.grid[row][::-1]
        self.grid.extend(bottom_half)

    # generate grids row-wise
    def generate_grid(self):
        # center row, row 7
        row_7 = self.generate_7th_row()
        self.grid.insert(0, row_7)
        self.update_col_depths()
        # next row, row 6
        row_6 = self.generate_6th_row()
        self.grid.insert(0, row_6)
        # rows 5-3:
        for row in range(3):
            row = self.generate_basic_row()
            self.grid.insert(0, row)
            self.update_col_depths()
        # row 2
        row_2 = self.generate_basic_row()
        self.grid.insert(0, row_2)
        # TODO: check to see if fully white row makes grid fully connected, if not, grid is invalid, start over
        while not self.is_fully_connected():
            row_2 = self.generate_basic_row()
            self.grid[0] = row_2
        self.update_col_depths()
        # rows 1,0
        for row in range(2):
            top_row = self.generate_top_row()
            self.grid.insert(0, top_row)
            self.update_col_depths()
        # mirror rows 0-6 to rows 14-8
        self.mirror_rows()

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
        for i in range(self.SIZE):
            for j in range(self.SIZE):
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
        for j in range(self.SIZE):
            col = self.grid[:][j]
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
print(test_grid.check_validity())
print(test_grid.word_count)
