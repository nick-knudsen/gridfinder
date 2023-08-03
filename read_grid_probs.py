import requests
from bs4 import BeautifulSoup


def parse_table(grid):
    data = []
    rows = grid.find_all('tr')
    for row in rows:
        row_return = []
        cols = row.find_all('td')
        for col in cols:
            value = col.attrs['data-pct']
            row_return.append(value)
        data.append(row_return)
    return data


url = 'https://www.xwordinfo.com/HeatMap'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html5lib')

grids = soup.find_all('table')

m_grid = grids[1]
t_grid = grids[2]
w_grid = grids[3]
r_grid = grids[4]
f_grid = grids[5]
s_grid = grids[6]

print(parse_table(m_grid))
