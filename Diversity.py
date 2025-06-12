"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1616/A -------------------------------------

You are given n integers a1,a2,…,an. 
You choose any subset of the given numbers (possibly, none or all numbers) and negate these numbers (i. e. change x→(−x)). 
What is the maximum number of different values in the array you can achieve?

Input
The first line of input contains one integer t (1 ≤ t ≤ 100): the number of test cases.

The next lines contain the description of the t test cases, two lines per a test case.

In the first line you are given one integer n (1 ≤ n ≤ 100): the number of integers in the array.

The second line contains n integers a1,a2,…,an (−100 ≤ a(i) ≤ 100).

Output
For each test case, print one integer: the maximum number of different elements in the array that you can achieve negating numbers in the array.

Input:
3
4
1 1 2 2
3
1 2 3
2
0 0

Output:
4
3
1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    diction = {}
    ans = 0
    for num in arr:
        temp = abs(num)
        if(temp in diction):
            diction[temp] += 1
        else:
            diction[temp] = 1
    for tk, tv in diction.items():
        if(tk == 0):
            ans += min(1, tv)
        else:
            ans += min(2, tv)
    print(ans)