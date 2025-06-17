"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2117/B --------------------------------

A shrink operation on an array a of size m is defined as follows:

Choose an index i (2≤i≤m−1) such that ai>ai−1 and ai > ai+1.
Remove a(i) from the array.
Define the score of a permutation∗ p as the maximum number of times that you can perform the shrink operation on p.

Yousef has given you a single integer n. 
Construct a permutation p of length n with the maximum possible score. If there are multiple answers, you can output any of them.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 10^3) — the number of test cases.

Each test case contains an integer n (3 ≤ n ≤ 2⋅10^5) — the size of the permutation.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output any permutation p1,p2,…,pn that maximizes the number of shrink operations.

Input:
2
3
6

Output:
1 3 2
2 3 6 4 5 1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    result = [1] + list(range(n, 1, -1))
    print(*result)