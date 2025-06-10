"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1905/A ------------------------------

Gridlandia has been hit by flooding and now has to reconstruct all of it's cities. Gridlandia can be described by an n×m matrix.

Initially, all of its cities are in economic collapse. The government can choose to rebuild certain cities. 
Additionally, any collapsed city which has at least one vertically neighboring rebuilt city and at least one horizontally neighboring rebuilt city can ask for aid from them and become 
rebuilt without help from the government. More formally, collapsed city positioned in (i,j) can become rebuilt if both of the following conditions are satisfied:

At least one of cities with positions (i+1,j) and (i−1,j) is rebuilt;
At least one of cities with positions (i,j+1) and (i,j−1) is rebuilt.
If the city is located on the border of the matrix and has only one horizontally or vertically neighbouring city, then we consider only that city.

The government wants to know the minimum number of cities it has to rebuild such that after some time all the cities can be rebuild.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of the test cases follows.

The only line of each test case contains two integers n and m (2 ≤ n, m ≤ 100) — the sizes of Gridlandia.

Output
For each test case, output a single integer — the minimum number of cities the government needs to rebuild.

Input:
3
2 2
5 7
3 2

Output:
2
7
3
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    print(max(n, m))