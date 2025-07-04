"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2030/B -------------------------------------- 

For an arbitrary binary string t, let f(t) be the number of non-empty subsequences† of t that contain only 0, and let g(t) be the number of non-empty subsequences of t that contain at least one 1. 
Note that for f(t) and for g(t), each subsequence is counted as many times as it appears in t. E.g., f(000)=7,g(100)=4. We define the oneness of the binary string t to be |f(t)−g(t)|, 
where for an arbitrary integer z, |z| represents the absolute value of z. You are given a positive integer n. Find a binary string s of length n such that its oneness is as small as possible. 
If there are multiple strings, you can print any of them.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The only line of each test case contains an integer n (1 ≤ n ≤ 2⋅10^5) — the length of s.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output s on a new line. If multiple answers exist, output any.

Input:
3
1
2
3

Output:
0
01
010
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    ans = "1"
    temp = "0" * (n - 1)
    print(ans + temp)