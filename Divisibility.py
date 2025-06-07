"""

--------------------------------------- Link for the challegne: https://codeforces.com/problemset/problem/1983/A ---------------------------------------

An array of integers a1,a2,⋯,an is beautiful subject to an integer k if it satisfies the following:

The sum of a(j) over all j such that j is a multiple of k and 1 ≤ j ≤ n, itself, is a multiple of k.
More formally, if ∑k|jaj is divisible by k for all 1 ≤ j ≤ n then the array a is beautiful subject to k. Here, the notation k|j means k divides j, that is, j is a multiple of k.
Given n
, find an array of positive nonzero integers, with each element less than or equal to 10^5 that is beautiful subject to all 1 ≤ k ≤ n.
It can be shown that an answer always exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first and only line of each test case contains a single integer n (1 ≤ n ≤ 100) — the size of the array.

Output
For each test case, print the required array as described in the problem statement.

Input:
3
3
6
7

Output:
4 22 18
10 6 15 32 125 54
23 18 27 36 5 66 7
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    for i in range(1, n + 1):
        print(i, end=' ')
    print()