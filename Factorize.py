"""
--------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1740/A ------------------------------

Pak Chanek has a prime number† n. Find a prime number m such that n+m is not prime.

† A prime number is a number with exactly 2 factors. The first few prime numbers are 2,3,5,7,11,13,…. In particular, 1 is not a prime number.

Input
Each test contains multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases. 
The following lines contain the description of each test case.

The only line of each test case contains a prime number n (2 ≤ n ≤ 10^5).

Output
For each test case, output a line containing a prime number m (2 ≤ m ≤ 10^5) such that n+m is not prime. 
It can be proven that under the constraints of the problem, such m always exists.

If there are multiple solutions, you can output any of them.

Input:
3
7
2
75619

Output:
2
7
47837
"""
cases = int(input())
firstPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 22, 29, 31, 37, 41, 43]
def is_prime(n):
    if(n < 2):
        return False
    if(n in (2, 3)):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if((n % i == 0) or (n % (i + 2) == 0)):
            return False
        i += 6
    return True
for _ in range(cases):
    num = int(input())
    for tempNum in firstPrimes:
        tempSum = num + tempNum
        if(not is_prime(tempSum)):
            print(tempNum)
            break