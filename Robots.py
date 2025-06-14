"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1680/B ---------------------------------

There is a field divided into n rows and m columns. 
Some cells are empty (denoted as E), other cells contain robots (denoted as R).

You can send a command to all robots at the same time. The command can be of one of the four types:

move up;
move right;
move down;
move left.

When you send a command, all robots at the same time attempt to take one step in the direction you picked. 
If a robot tries to move outside the field, it explodes; otherwise, every robot moves to an adjacent cell in the chosen direction.

You can send as many commands as you want (possibly, zero), in any order. 
Your goal is to make at least one robot reach the upper left corner of the field. Can you do this without forcing any of the robots to explode?

Input
The first line contains one integer t (1 ≤ t ≤ 5000) — the number of test cases.

Each test case starts with a line containing two integers n and m (1 ≤ n, m ≤ 5) — the number of rows and the number of columns, respectively. 
Then n lines follow; each of them contains a string of m characters. Each character is either E (empty cell} or R (robot).

Additional constraint on the input: in each test case, there is at least one robot on the field.

Output
If it is possible to make at least one robot reach the upper left corner of the field so that no robot explodes, print YES. Otherwise, print NO.

Input:
6
1 3
ERR
2 2
ER
RE
2 2
ER
ER
1 1
R
4 3
EEE
EEE
ERR
EER
3 3
EEE
EER
REE

Output:
YES
NO
YES
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    ok = True

    rs = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'R']

    targetR = min(rs, key=lambda x:(x[0], x[1]))
    targetX, targetY = targetR

    moveUp = targetX
    moveLeft = targetY

    for x, y in rs:
        newX = x - moveUp
        newY = y - moveLeft

        if(newX < 0 or newY < 0):
            ok = False
            break
    print("YES" if ok else "NO")