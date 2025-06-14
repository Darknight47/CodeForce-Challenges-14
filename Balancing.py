"""

------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1661/A ------------------------------------

You are given two arrays of length n: a1,a2,…,an and b1,b2,…,bn.

You can perform the following operation any number of times:

Choose integer index i (1 ≤ i ≤ n);
Swap ai and bi.
What is the minimum possible sum |a1−a2|+|a2−a3|+⋯+|an−1−an| + |b1−b2|+|b2−b3|+⋯+|bn−1−bn| (in other words, ∑i=1n−1(|ai−ai+1|+|bi−bi+1|)) you can achieve after performing several 
(possibly, zero) operations?

Input
The first line contains a single integer t (1 ≤ t ≤ 4000) — the number of test cases. Then, t test cases follow.

The first line of each test case contains the single integer n (2 ≤ n ≤ 25) — the length of arrays a and b.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤10^9) — the array a.

The third line of each test case contains n integers b1,b2,…,bn (1≤bi≤10^9) — the array b.

Output
For each test case, print one integer — the minimum possible sum ∑i=1n−1(|ai−ai+1|+|bi−bi+1|).

Input:
3
4
3 3 10 10
10 10 3 3
5
1 2 3 4 5
6 7 8 9 10
6
72 101 108 108 111 44
10 87 111 114 108 100

Output:
0
8
218
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    dp0, dp1 = 0, 0
    for i in range(1, sze):
        noSwap_0 = dp0 + abs(arr[i] - arr[i - 1]) + abs(brr[i] - brr[i - 1])
        swap_0 = dp0 + abs(brr[i] - arr[i - 1]) + abs(arr[i] - brr[i - 1])
        
        noSwap_1 = dp1 + abs(arr[i] - brr[i-1]) + abs(brr[i] - arr[i-1])
        swap_1 = dp1 + abs(brr[i] - brr[i-1]) + abs(arr[i] - arr[i-1])

        new_dp0 = min(noSwap_0, noSwap_1)
        new_dp1 = min(swap_0, swap_1)

        dp0, dp1 = new_dp0, new_dp1
    print(min(dp0, dp1))