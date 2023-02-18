# Contains encoding for crossword grid
from tkinter import Grid
import pandas as pd
import numpy as np

# How large to make the grid
GRID_SIZE = 7

# Initial probability of box being empty (will contain letter)
P = 0.84

#Grid Rules
MIN_WORDS = 10
MAX_WORDS = 30
MIN_WORD_LENGTH = 3

# Contains grid shape
# true if box is empty (will contain letter), false if box is black
grid = np.random.choice(a=[True, False], size=(GRID_SIZE, GRID_SIZE), p=[P, 1-P])

# calculate grid stats

# counting number of words in a crossword grid:
#   if a box above or left of a given box is black (false), current box
#   is the first letter of a new word

# finding shortest word:
# slice grid vertically and horizontally
# find shortest substring of true values

print(grid)


