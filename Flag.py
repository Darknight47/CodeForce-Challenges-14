"""
--------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1534/A --------------------------

Today we will be playing a red and white colouring game (no, this is not the Russian Civil War; these are just the colours of the Canadian flag).

You are given an n×m grid of "R", "W", and "." characters. "R" is red, "W" is white and "." is blank. The neighbours of a cell are those that share an edge with it (those that only share a corner do not count).

Your job is to colour the blank cells red or white so that every red cell only has white neighbours (and no red ones) and every white cell only has red neighbours (and no white ones). 
You are not allowed to recolour already coloured cells.

Input
The first line contains t (1 ≤ t ≤ 100), the number of test cases.

In each test case, the first line will contain n (1 ≤ n ≤ 50) and m (1 ≤ m ≤ 50), the height and width of the grid respectively.

The next n lines will contain the grid. Each character of the grid is either 'R', 'W', or '.'.

Output
For each test case, output "YES" if there is a valid grid or "NO" if there is not.

If there is, output the grid on the next n lines. If there are multiple answers, print any.

In the output, the "YES"s and "NO"s are case-insensitive, meaning that outputs such as "yEs" and "nO" are valid. However, the grid is case-sensitive.

Input:
3
4 6
.R....
......
......
.W....
4 4
.R.W
....
....
....
5 1
R
W
R
W
R

Output:
YES
WRWRWR
RWRWRW
WRWRWR
RWRWRW
NO
YES
R
W
R
W
R
"""
def fill_grid(grid):
    n, m = len(grid), len(grid[0])
    colors = ['R', 'W']

    def is_valid(start):
        filled = []
        for i in range(n):
            row = ''
            for j in range(m):
                expected = colors[(i + j + start) % 2]
                cell = grid[i][j]
                if cell != '.' and cell != expected:
                    return None  # Conflict found
                row += expected if cell == '.' else cell
            filled.append(row)
        return filled

    # Try both color patterns
    result = is_valid(0) or is_valid(1)
    if result:
        print("YES")
        for row in result:
            print(row)
    else:
        print("NO")

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    fill_grid(grid)
    print("---------------------------------")