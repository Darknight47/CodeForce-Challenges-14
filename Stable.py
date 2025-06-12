"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1621/A -------------------------------------

You have an n×n chessboard and k rooks. 
Rows of this chessboard are numbered by integers from 1 to n from top to bottom and columns of this chessboard are numbered by integers from 1 to n from left to right. 
The cell (x,y) is the cell on the intersection of row x and collumn y for 1 ≤ x ≤ n and 1 ≤ y ≤ n.

The arrangement of rooks on this board is called good, if no rook is beaten by another rook.

A rook beats all the rooks that shares the same row or collumn with it.

The good arrangement of rooks on this board is called not stable, if it is possible to move one rook to the adjacent cell so arrangement becomes not good. 
Otherwise, the good arrangement is stable. Here, adjacent cells are the cells that share a side.

Please, find any stable arrangement of k rooks on the n×n chessboard or report that there is no such arrangement.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains two integers n, k (1 ≤ k ≤ n ≤ 40) — the size of the chessboard and the number of rooks.

Output
If there is a stable arrangement of k rooks on the n×n chessboard, output n lines of symbols "." and "R". 
The j-th symbol of the i-th line should be equals R if and only if there is a rook on the cell (i,j) in your arrangement.

If there are multiple solutions, you may output any of them.

If there is no stable arrangement, output −1.

Input:
5
3 2
3 3
1 1
5 2
40 33

Output:
..R
...
R..
-1
R
.....
R....
.....
....R
.....
-1
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    rooks = k
    positions = set()
    for i in range(0, n, 2):
        if(k > 0):
            tempTuple = (i, i)
            positions.add(tempTuple)
        k -= 1
    if(k <= 0):
        for i in range(n):
            row = ""
            for j in range(n):
                if i % 2 == 0 and (i, j) in positions:
                    row += "R"
                    rooks -= 1
                else:
                    row += "."
            print(row)
    else:
        print("-1")