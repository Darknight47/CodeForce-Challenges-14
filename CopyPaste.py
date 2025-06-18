"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1417/A ------------------------------

BThero is a powerful magician. He has got n piles of candies, the i-th pile initially contains a(i) candies. BThero can cast a copy-paste spell as follows:

He chooses two piles (i,j) such that 1 ≤ i,j ≤ n and i≠j.
All candies from pile i are copied into pile j. Formally, the operation aj:=aj+ai is performed.

 BThero can cast this spell any number of times he wants to — but unfortunately, if some pile contains strictly more than k
candies, he loses his magic power. What is the maximum number of times BThero can cast the spell without losing his power?

Input
The first line contains one integer T (1 ≤ T ≤ 500) — the number of test cases.

Each test case consists of two lines:

the first line contains two integers n and k (2 ≤ n ≤ 1000, 2 ≤ k ≤ 10^4);

the second line contains n integers a1, a2, ..., an (1 ≤ a(i) ≤ k).
It is guaranteed that the sum of n over all test cases does not exceed 1000, and the sum of k over all test cases does not exceed 10^4.

Output
For each test case, print one integer — the maximum number of times BThero can cast the spell without losing his magic power.

Input:
3
2 2
1 1
3 5
1 2 3
3 7
3 2 2

Output:
1
5
4
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    minNum = arr[0]
    ans = 0
    for i in range(1, n):
        maxAdd = (k - arr[i]) // minNum
        if(maxAdd > 0):
            ans += maxAdd
    print(ans)