"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1902/A ------------------------------------

You are given a string s, consisting only of characters '0' and/or '1'.

In one operation, you choose a position i from 1 to |s|−1, where |s| is the current length of string s. 
Then you insert a character between the i-th and the (i+1)-st characters of s. If si=si+1, you insert '1'. If si≠si+1, you insert '0'.

Is it possible to make the number of zeroes in the string strictly greater than the number of ones, using any number of operations (possibly, none)?

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of testcases.

The first line of each testcase contains an integer n (1 ≤ n ≤ 100).

The second line contains a string s of length exactly n, consisting only of characters '0' and/or '1'.

Output
For each testcase, print "YES" if it's possible to make the number of zeroes in s strictly greater than the number of ones, using any number of operations (possibly, none). 
Otherwise, print "NO".

Input:
3
2
00
2
11
2
10

Output:
YES
NO
YES
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    ok = False
    if(sze > 1):
        for i in range(sze - 1):
            first = s[i]
            second = s[i + 1]
            if(first != second or first == '0' and second == '0'):
                ok = True
                break
    else:
        if(s[0] == '0'):
            ok = True
    print("YES" if ok else "NO")