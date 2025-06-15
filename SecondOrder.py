"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/22/A -------------------------------

Once Bob needed to find the second order statistics of a sequence of integer numbers. Lets choose each number from the sequence exactly once and sort them. 
The value on the second position is the second order statistics of the given sequence. In other words it is the smallest element strictly greater than the minimum. 
Help Bob solve this problem.

Input
The first input line contains integer n (1 ≤ n ≤ 100) — amount of numbers in the sequence. 
The second line contains n space-separated integer numbers — elements of the sequence. These numbers don't exceed 100 in absolute value.

Output
If the given sequence has the second order statistics, output this order statistics, otherwise output NO.

Input:
4
1 2 2 -4

Output:
1
"""
sze = int(input())
tempSet = set(map(int, input().split()))
sortedSet = sorted(tempSet)
if(len(sortedSet) >= 2):
    print(sortedSet[1])
else:
    print("NO")