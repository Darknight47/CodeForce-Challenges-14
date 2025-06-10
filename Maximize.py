"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1991/A --------------------------------------

You are given an array a of n integers, where n is odd.

In one operation, you will remove two adjacent elements from the array a, and then concatenate the remaining parts of the array. 
For example, given the array [4,7,4,2,9], we can obtain the arrays [4,2,9] and [4,7,9] by the operations [4,7––––,4,2,9]→[4,2,9] and [4,7,4,2––––,9]→[4,7,9] respectively. 
However, we cannot obtain the array [7,2,9] as it requires deleting non-adjacent elements [4–,7,4–,2,9].

You will repeatedly perform this operation until exactly one element remains in a.

Find the maximum possible value of the remaining element in a.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 99; n is odd) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100) — the elements of the array a.

Note that there is no bound on the sum of n over all test cases.

Output
For each test case, output a single integer — the maximum possible value of the remaining element in a.

Input:
4
1
6
3
1 3 2
5
4 7 4 2 9
7
3 1 4 1 5 9 2

Output:
6
2
9
5
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(0, sze, 2):
        ans = max(ans, arr[i])
    print(ans)