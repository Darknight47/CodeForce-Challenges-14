"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1712/A ------------------------------

You are given a permutation p1,p2,…,pn of length n and a positive integer k ≤ n.

In one operation you can choose two indices i and j (1 ≤ i < j ≤ n) and swap pi with pj.

Find the minimum number of operations needed to make the sum p1+p2+…+pk as small as possible.

A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). Description of the test cases follows.

The first line of each test case contains two integers n and k (1 ≤ k ≤ n ≤ 100).

The second line of each test case contains n integers p1,p2,…,pn (1 ≤ p(i) ≤ n). It is guaranteed that the given numbers form a permutation of length n.

Output
For each test case print one integer — the minimum number of operations needed to make the sum p1+p2+…+pk as small as possible.

Input:
4
3 1
2 3 1
3 3
1 2 3
4 2
3 4 1 2
1 1
1

Output:
1
0
2
0
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    sortedArr = sorted(arr)
    ans = 0
    tempSorted = sortedArr[k - 1]
    for i in range(k):
        if(arr[i] > tempSorted):
            ans += 1
    print(ans)