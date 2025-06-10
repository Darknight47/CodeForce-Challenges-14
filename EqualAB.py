"""
----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1736/A -----------------------------

You are given two arrays a and b of n elements, each element is either 0 or 1.

You can make operations of 2 kinds.

Pick an index i and change a(i) to 1−a(i).
Rearrange the array a however you want. Find the minimum number of operations required to make a equal to b.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 400) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the arrays a and b.

The second line of each test case contains n space-separated integers a1,a2,…,an (a(i) is 0 or 1), representing the array a.

The third line of each test case contains n space-separated integers b1,b2,…,bn (b(i) is 0 or 1), representing the array b.

Output
For each test case, print the minimum number of operations required to make a equal to b.

Input:
5
3
1 0 1
0 0 1
4
1 1 0 0
0 1 1 1
2
1 1
1 1
4
1 0 0 1
0 1 1 0
1
0
1

Output:
1
2
0
1
1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    arrOnes = arr.count(1)
    brrOnes = brr.count(1)
    diff = abs(arrOnes - brrOnes)
    mismatch = 0
    for i in range(sze):
        if(arr[i] != brr[i]):
            mismatch += 1
    ans = min(mismatch, diff + 1)
    print(ans)