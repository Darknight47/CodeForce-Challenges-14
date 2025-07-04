"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/746/A ------------------------------------

Nikolay has a lemons, b apples and c pears. He decided to cook a compote. According to the recipe the fruits should be in the ratio 1: 2: 4. 
It means that for each lemon in the compote should be exactly 2 apples and exactly 4 pears. You can't crumble up, break up or cut these fruits into pieces. 
These fruits — lemons, apples and pears — should be put in the compote as whole fruits.

Your task is to determine the maximum total number of lemons, apples and pears from which Nikolay can cook the compote. 
It is possible that Nikolay can't use any fruits, in this case print 0.

Input
The first line contains the positive integer a (1 ≤ a ≤ 1000) — the number of lemons Nikolay has.

The second line contains the positive integer b (1 ≤ b ≤ 1000) — the number of apples Nikolay has.

The third line contains the positive integer c (1 ≤ c ≤ 1000) — the number of pears Nikolay has.

Output
Print the maximum total number of lemons, apples and pears from which Nikolay can cook the compote.

Input:
2
5
7

Output:
7
"""
a = int(input())
b = int(input())
c = int(input())
tempMin = min(a, b//2, c//4)
ans = tempMin * 7
print(ans)