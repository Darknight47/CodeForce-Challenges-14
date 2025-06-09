"""
----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1828/A -----------------------------

You are given a positive integer n. Please find an array a1,a2,…,an that is perfect.

A perfect array a1,a2,…,an satisfies the following criteria:

1 ≤ a(i) ≤ 1000 for all 1 ≤ i ≤ n.
a(i) is divisible by i for all 1 ≤ i ≤ n.
a1+a2+…+an is divisible by n.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 200). The description of the test cases follows.

The only line of each test case contains a single positive integer n (1 ≤ n ≤ 200) — the length of the array a.

Output
For each test case, output an array a1,a2,…,an that is perfect.

We can show that an answer always exists. If there are multiple solutions, print any.

Input:
7
1
2
3
4
5
6
7

Output:
1
2 4
1 2 3
2 8 6 4
3 4 9 4 5
1 10 18 8 5 36
3 6 21 24 10 6 14
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(range(1, n + 1))
    tempSum = sum(arr)
    cpySum = tempSum
    if(tempSum % 2 == n):
        print(*arr)
    else:
        while tempSum % n != 0:
            tempSum += 1
        diff = tempSum - cpySum
        if(diff > 0):
            arr[0] += diff
        print(*arr)