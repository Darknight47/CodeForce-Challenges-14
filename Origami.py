"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1080/A --------------------------------

Petya is having a party soon, and he has decided to invite his n friends.

He wants to make invitations in the form of origami. For each invitation, he needs two red sheets, five green sheets, and eight blue sheets. 
The store sells an infinite number of notebooks of each color, but each notebook consists of only one color with k sheets. 
That is, each notebook contains k sheets of either red, green, or blue.

Find the minimum number of notebooks that Petya needs to buy to invite all n of his friends.

Input
The first line contains two integers n and k (1 ≤ n, k ≤ 10^8) — the number of Petya's friends and the number of sheets in each notebook respectively.

Output
Print one number — the minimum number of notebooks that Petya needs to buy.

Input:
3 5
Output:
10
"""
import math
n, k = map(int, input().split())
redNeeded = n * 2
greenNeeded = n * 5
blueNeeded = n * 8
redNotebooks = math.ceil(redNeeded / k)
greenNotebooks = math.ceil(greenNeeded / k)
blueNotebooks = math.ceil(blueNeeded / k)
print(redNotebooks + greenNotebooks + blueNotebooks)