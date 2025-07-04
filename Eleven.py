"""


Eleven wants to choose a new name for herself. As a bunch of geeks, her friends suggested an algorithm to choose a name for her. Eleven wants her name to have exactly n characters.

Her friend suggested that her name should only consist of uppercase and lowercase letters 'O'. 
More precisely, they suggested that the i-th letter of her name should be 'O' (uppercase) if i is a member of Fibonacci sequence, and 'o' (lowercase) otherwise. 
The letters in the name are numbered from 1 to n. Fibonacci sequence is the sequence f where

f1 = 1,
f2 = 1,
fn = fn - 2 + fn - 1 (n > 2).
As her friends are too young to know what Fibonacci sequence is, they asked you to help Eleven determine her new name.

Input
The first and only line of input contains an integer n (1 ≤ n ≤ 1000).

Output
Print Eleven's new name on the first and only line of output.

Input:
8
Output:
OOOoOooO
"""
sze = int(input())
fib = set()
a, b = 0, 1
while a <= sze:
    fib.add(a)
    a, b = b, a + b

ans = ""
for i in range(1, sze + 1):
    ans += "O" if i in fib else 'o'
print(ans)