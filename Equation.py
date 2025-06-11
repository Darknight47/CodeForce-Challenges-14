"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1269/A -------------------------------------

Let's call a positive integer composite if it has at least one divisor other than 1 and itself. For example:

the following numbers are composite: 1024, 4, 6, 9;
the following numbers are not composite: 13, 1, 2, 3, 37.
You are given a positive integer n. Find two composite integers a,b such that a−b=n.

It can be proven that solution always exists.

Input
The input contains one integer n (1 ≤ n ≤ 10^7): the given integer.

Output
Print two composite integers a,b (2 ≤ a, b ≤ 10^9,a−b=n).

It can be proven, that solution always exists.

If there are several possible solutions, you can print any.

Input:
1

Output:
9 8
"""
def is_composite(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False  # It's prime if no divisors found

n = int(input())
a = 4
while True:
    b = a - n
    if(b > 0 and is_composite(b) and is_composite(a)):
        print(a, b)
        break
    a += 1