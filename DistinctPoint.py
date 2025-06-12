"""
----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1108/A -------------------------------------

You are given two segments [l1;r1] and [l2;r2] on the x-axis. It is guaranteed that l1<r1 and l2 < r2. 
Segments may intersect, overlap or even coincide with each other.

Your problem is to find two integers a and b such that l1≤a≤r, l2≤b≤r2 and a≠b. 
In other words, you have to choose two distinct integer points in such a way that the first point belongs to the segment [l1;r1] and the second one belongs to the segment [l2;r2].

It is guaranteed that the answer exists. If there are multiple answers, you can print any of them.

You have to answer q independent queries.

Input
The first line of the input contains one integer q (1 ≤ q ≤ 500) — the number of queries.

Each of the next q lines contains four integers l1i,r1i,l2i and r2(i) (1 ≤ l1i, r1i, l2i, r2i ≤ 10^9, l1i < r1i, l2i < r2i) — the ends of the segments in the i-th query.

Output
Print 2q integers. For the i-th query print two integers a(i) and b(i) — such numbers that l1(i) ≤ a(i) ≤ r1(i), l2i≤bi≤r2i and a(i) ≠ b(i). 
Queries are numbered in order of the input.

It is guaranteed that the answer exists. If there are multiple answers, you can print any.

Input:
5
1 2 1 2
2 6 3 4
2 4 1 3
1 2 1 3
1 4 5 8

Output:
2 1
3 4
3 2
1 2
3 7
"""
cases = int(input())
for i in range(cases):
    l, r, ll, rr = map(int, input().split())
    if(l != ll):
        print(l, ll)
    elif(l != rr):
        print(l, rr)
    elif(r != ll):
        print(r, ll)
    elif(r != rr):
        print(r, rr)