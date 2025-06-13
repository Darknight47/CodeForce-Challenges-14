"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1923/A ---------------------------------

There is a ribbon divided into n cells, numbered from 1 to n from left to right. Each cell either contains a chip or is free.

You can perform the following operation any number of times (possibly zero): choose a chip and move it to the closest free cell to the left. 
You can choose any chip that you want, provided that there is at least one free cell to the left of it. When you move the chip, 
the cell where it was before the operation becomes free.

Your goal is to move the chips in such a way that they form a single block, without any free cells between them. 
What is the minimum number of operations you have to perform?

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer n (2 ≤ n ≤ 50) — the number of cells;
the second line contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 1); ai=0 means that the i-th cell is free; ai=1 means that the i-th cell contains a chip.

Additional constraint on the input: in each test case, at least one cell contains a chip.

Output
For each test case, print one integer — the minimum number of operations you have to perform so that all chips form a single block without any free cells between them.

Input:
5
8
0 1 1 1 0 1 1 0
6
0 1 0 0 0 0
6
1 1 1 1 1 1
5
1 0 1 0 1
9
0 1 1 0 0 0 1 1 0

Output:
1
0
0
2
3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input().replace(" ", "")
    ones_indices = [i for i, bit in enumerate(s) if bit == '1']
    zero_count = 0

    for i in range(len(ones_indices) - 1):  # Iterate between consecutive 1s
        start, end = ones_indices[i], ones_indices[i + 1]
        zero_count += s[start + 1:end].count('0')

    print(zero_count)