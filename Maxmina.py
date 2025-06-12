"""
---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1746/A ---------------------------------------

You have an array a of size n consisting only of zeroes and ones and an integer k. 
In one operation you can do one of the following:

Select 2 consecutive elements of a and replace them with their minimum (that is, let a:=[a1,a2,…,ai−1,min(ai,ai+1),ai+2,…,an] for some 1≤i≤n−1). 
This operation decreases the size of a by 1.
Select k consecutive elements of a and replace them with their maximum (that is, let a:=[a1,a2,…,ai−1,max(ai,ai+1,…,ai+k−1),ai+k,…,an] for some 1 ≤ i ≤ n−k + 1). 
This operation decreases the size of a by k−1.
Determine if it's possible to turn a into [1] after several (possibly zero) operations.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The first line of each test case contains two integers n and k (2 ≤ k ≤ n ≤ 50), the size of array a and the length of segments that you can perform second type operation on.

The second line contains n integers a1,a2,…,an (a(i) is 0 or 1), elements of array a.

Output
For each test case, if it is possible to turn a into [1], print "YES", otherwise print "NO".

Input:
7
3 2
0 1 0
5 3
1 0 1 1 0
2 2
1 1
4 4
0 0 0 0
6 3
0 0 1 0 0 1
7 5
1 1 1 1 1 1 1
5 3
0 0 1 0 0

Output:
YES
YES
YES
NO
YES
YES
YES
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ones = arr.count(1)
    if(ones >= 1):
        print("YES")
    else:
        print("NO")