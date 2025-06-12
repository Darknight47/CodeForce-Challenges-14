"""
----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1492/A -------------------------------------

Three swimmers decided to organize a party in the swimming pool! At noon, they started to swim from the left side of the pool.

It takes the first swimmer exactly a minutes to swim across the entire pool and come back, exactly b minutes for the second swimmer and c minutes for the third. 
Hence, the first swimmer will be on the left side of the pool after 0, a, 2a, 3a, ... minutes after the start time, the second one will be at 0, b, 2b, 3b, ... minutes, 
and the third one will be on the left side of the pool after 0, c, 2c, 3c, ... minutes.

You came to the left side of the pool exactly p minutes after they started swimming. Determine how long you have to wait before one of the swimmers arrives at the left side of the pool.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Next t lines contains test case descriptions, one per line.

Each line contains four integers p, a, b and c (1 ≤p,a,b,c ≤ 10^18), time in minutes after the start, when you came to the pool and times in minutes it take the swimmers to cross the entire pool and come back.

Output
For each test case, output one integer — how long you have to wait (in minutes) before one of the swimmers arrives at the left side of the pool.

Input:
4
9 5 4 8
2 6 10 9
10 2 5 10
10 9 9 9

Output:
1
4
0
8
"""
cases = int(input())
for _ in range(cases):
    p, a, b, c = map(int, input().split())
    
    waitA = ((p + a - 1) // a) * a - p
    waitB = ((p + b - 1) // b) * b - p
    waitC = ((p + c - 1) // c) * c - p
    print(min(waitA, waitB, waitC))