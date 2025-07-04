"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1392/B -------------------------------

Being stuck at home, Ray became extremely bored. To pass time, he asks Lord Omkar to use his time bending power: Infinity Clock! 
However, Lord Omkar will only listen to mortals who can solve the following problem:

You are given an array a of n integers. You are also given an integer k. 
Lord Omkar wants you to do k operations with this array.

Define one operation as the following:

Set d to be the maximum value of your array.
For every i from 1 to n, replace ai with d−ai.
The goal is to predict the contents in the array after k operations. Please help Ray determine what the final sequence will look like!

Input
Each test contains multiple test cases. The first line contains the number of cases t (1 ≤ t ≤ 100). Description of the test cases follows.

The first line of each test case contains two integers n and k (1 ≤ n ≤ 2⋅10^5, 1 ≤ k ≤ 10^18) – the length of your array and the number of operations to perform.

The second line of each test case contains n integers a1,a2,...,an (−10^9 ≤ a(i) ≤ 10^9) – the initial contents of your array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each case, print the final version of array a after k operations described above.

Input:
3
2 1
-199 192
5 19
5 -1 4 2 0
1 2
69

Output:
391 0
0 6 1 3 5
0
"""
def op(arr):
    M = max(arr)
    return [M - a for a in arr]

cases = int(input())
for _ in range(cases):
    sze, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if(k == 0):
        print(*arr)
    else:      
        arr1 = op(arr)
        if(k == 1):
            print(*arr1)
        else:
            arr2 = op(arr1)
            if(k % 2 == 1):
                print(*arr1)
            else:
                print(*arr2)