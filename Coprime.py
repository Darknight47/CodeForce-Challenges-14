"""
---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2063/A --------------------------------------------

A segment of positive integers [l,r] is called coprime if l and r are coprime∗.

A coprime segment [l,r] is called minimal coprime if it does not contain† any coprime segment not equal to itself. To better understand this statement, you can refer to the notes.

Given [l,r], a segment of positive integers, find the number of minimal coprime segments contained in [l,r].

∗ Two integers a and b are coprime if they share only one positive common divisor. 
For example, the numbers 2 and 4 are not coprime because they are both divided by 2 and 1, but the numbers 7 and 9 are coprime because their only positive common divisor is 1.

†A segment [l′,r′] is contained in the segment [l,r] if and only if l ≤ l′ ≤ r′ ≤ r.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The only line of each test case consists of two integers l and r (1 ≤ l ≤ r ≤ 10^9).

Output
For each test case, output the number of minimal coprime segments contained in [l,r], on a separate line.

Input:
6
1 2
1 10
49 49
69 420
1 1
9982 44353

Output:
1
9
0
351
1
34371
"""
cases = int(input())
for _ in range(cases):
    l, r = map(int, input().split())
    if(l == r and r == 1):
        print(1)
    else:
        print(r - l)