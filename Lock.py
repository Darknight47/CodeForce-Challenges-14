"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2048/A -----------------------------------------

Kevin is trapped in Lakeside Village by Grace. At the exit of the village, there is a combination lock that can only be unlocked if Kevin solves it.

The combination lock starts with an integer x. 
Kevin can perform one of the following two operations zero or more times:

If x≠33, he can select two consecutive digits 3 from x and remove them simultaneously. For example, if x=13323, he can remove the second and third 3, changing x to 123.
If x ≥ 33, he can change x to x−33. For example, if x=99, he can choose this operation to change x to 99−33=66.
When the value of x on the combination lock becomes 0, Kevin can unlock the lock and escape from Lakeside Village. Please determine whether it is possible for Kevin to unlock the combination lock and escape.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4).

The only line of each test case contains a positive integer x (1 ≤ x ≤ 10^9).

Output
For each test case, output "YES" or "NO" (without quotes) in one line, representing whether Kevin can unlock the combination lock and escape. You can output the answer in any case (upper or lower). 
For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
5
165
6369
666
114514
133333332

Output:
YES
YES
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    print("YES" if num % 33 == 0 else "NO")