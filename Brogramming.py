"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2064/A --------------------------------

One day after waking up, your friend challenged you to a brogramming contest. 
In a brogramming contest, you are given a binary string∗ s of length n and an initially empty binary string t. 
During a brogramming contest, you can make either of the following moves any number of times:

remove some suffix† from s and place it at the end of t, or remove some suffix from t and place it at the end of s.
To win the brogramming contest, you must make the minimum number of moves required to make s contain only the character 0 and t contain only the character 1. 
Find the minimum number of moves required.
∗A binary string is a string consisting of characters 0 and 1.

† A string a is a suffix of a string b if a can be obtained from deletion of several (possibly, zero or all) elements from the beginning of b.

Input
The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case is an integer n (1 ≤ n ≤ 1000) — the length of the string s.

The second line of each test case contains the binary string s.

The sum of n across all test cases does not exceed 1000.

Output
For each testcase, output the minimum number of moves required.

Input:
5
5
00110
4
1111
3
001
5
00000
3
101

Output:
2
1
1
0
3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    ans = 0
    for i in range(sze - 1):
        first = s[i]
        second = s[i + 1]
        if(first != second):
            ans += 1
    if(s[0] == '1'):
        ans += 1
    print(ans)