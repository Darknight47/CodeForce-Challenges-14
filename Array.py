"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2069/A --------------------------------------

For an array of integers a1,a2,…,an, we define its equality characteristic as the array b2,b3,…,bn−1, where bi=1 if the i-th element of the array a is equal 
to both of its neighbors, and bi=0 if the i-th element of the array a is not equal to at least one of its neighbors.

For example, for the array [1,2,2,2,3,3,4,4,4,4], the equality characteristic will be [0,1,0,0,0,0,1,1].

You are given the array b2,b3,…,bn−1. 
Your task is to determine whether there exists such an array a for which the given array is the equality characteristic.

Input
The first line contains one integer t (1 ≤ t≤ 1 000) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer n (3 ≤ n ≤ 100);

the second line contains n−2 integers b2,b3,…,bn−1 (0 ≤ b(i) ≤ 1).

Output
For each test case, output YES if the array a exists, or NO if such an array does not exist. Each letter can be printed in any case.

Input:
3
10
0 1 0 0 0 0 1 1
3
1
10
0 1 0 1 1 0 0 1

Output:
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input().strip()
    s = s.replace(" ", "")
    if("101" in s):
        print("NO")
    else:
        print("YES")