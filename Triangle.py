"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1064/A ------------------------------------

Masha has three sticks of length a, b and c centimeters respectively. 
In one minute Masha can pick one arbitrary stick and increase its length by one centimeter. She is not allowed to break sticks.

What is the minimum number of minutes she needs to spend increasing the stick's length in order to be able to assemble a triangle of positive area. 
Sticks should be used as triangle's sides (one stick for one side) and their endpoints should be located at triangle's vertices.

Input
The only line contains tree integers a, b and c (1 ≤ a, b, c ≤ 100) — the lengths of sticks Masha possesses.

Output
Print a single integer — the minimum number of minutes that Masha needs to spend in order to be able to make the triangle of positive area from her sticks.

Input:
3 4 5

Output:
0
"""
a, b, c = map(int, input().split())
arr = [a, b, c]
arr.sort()
ans = max(0, arr[2] - (arr[1] + arr[0]) + 1)
print(ans)