"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1694/A -------------------------------------

Define the score of some binary string T as the absolute difference between the number of zeroes and ones in it. 
(for example, T= 010001 contains 4 zeroes and 2 ones, so the score of T is |4−2|=2).

Define the creepiness of some binary string S as the maximum score among all of its prefixes 
(for example, the creepiness of S= 01001 is equal to 2 because the score of the prefix S[1…4] is 2 and the rest of the prefixes have a score of 2 or less).

Given two integers a and b, construct a binary string consisting of a zeroes and b ones with the minimum possible creepiness.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000)— the number of test cases. The description of the test cases follows.

The only line of each test case contains two integers a and b (1 ≤ a, b ≤ 100)  — the numbers of zeroes and ones correspondingly.

Output
For each test case, print a binary string consisting of a zeroes and b ones with the minimum possible creepiness. If there are multiple answers, print any of them.

Input:
5
1 1
1 2
5 2
4 5
3 7

Output:
10
011
0011000
101010101
0001111111
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    ans = ""
    while a > 0 or b > 0:
        if(a > 0):
            ans += '0'
            a -= 1
        if(b > 0):
            ans += '1'
            b -= 1
    print(ans)