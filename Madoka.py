"""
---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1647/A ----------------------------------------

Madoka finally found the administrator password for her computer. 
Her father is a well-known popularizer of mathematics, so the password is the answer to the following problem.

Find the maximum decimal number without zeroes and with no equal digits in a row, such that the sum of its digits is n.

Madoka is too tired of math to solve it herself, so help her to solve this problem!

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Description of the test cases follows.

The only line of each test case contains an integer n (1 ≤ n ≤ 1000) — the required sum of the digits.

Output
For each test case print the maximum number you can obtain.

Input:
5
1
2
3
4
5

Output:
1
2
21
121
212
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n <= 2):
        print(n)
    else:
        if(n % 3 == 1):
            start = [1]
            addOne = False
        else:
            start = [2]
            addOne = True
        tempSum = start[0]
        while True:
            if(tempSum >= n):
                break
            if(addOne):
                start.append(1)
                addOne = False
                tempSum += 1
            else:
                start.append(2)
                addOne = True
                tempSum += 2
        print("".join(map(str, start)))            