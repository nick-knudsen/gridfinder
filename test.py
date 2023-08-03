import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def is_fully_connected(grid):
        visited_cells = []
        cell_status = np.full((len(grid),8), False)

        # visit first unvisited cell
        break_next = False
        for i in range(len(grid)):
            if break_next:
                break
            for j in range(len(grid[i])):
                if grid[i][j]:
                    visited_cells.append((i,j))
                    cell_status[i][j] = True
                    break_next = True
                    break
        while visited_cells:
            cell = visited_cells[0]
            row = cell[0]
            col = cell[1]
            for adj_row, adj_col in zip((-1,0,0,1), (0,-1,1,0)):
                new_row = row+adj_row
                new_col = col+adj_col
                if new_row < 0 or new_row > len(grid)-1 or new_col < 0 or new_col > len(grid[0])-1:
                    continue
                if grid[new_row][new_col] and not cell_status[new_row][new_col]:
                    cell_status[new_row][new_col] = True
                    visited_cells.append((new_row, new_col))
                
            visited_cells.pop(0)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and not cell_status[i][j]:
                    return False
        return True


def get_grid_weights():
    tables = pd.read_html('https://www.xwordinfo.com/HeatMap', flavor='html5lib')
    m_df = tables[1]
    t_df = tables[2]
    w_df = tables[3]
    r_df = tables[4]
    f_df = tables[5]
    s_df = tables[6]

    print(m_df.info())

get_grid_weights()

# test_grid = [
#     [1,0,1,1,1,1,0,1],
#     [1,0,0,1,0,1,0,1],
#     [1,1,0,1,0,1,0,1],
#     [0,1,0,1,0,1,0,1],
#     [1,1,1,1,0,1,1,1]
# ]

#print(is_fully_connected(test_grid))