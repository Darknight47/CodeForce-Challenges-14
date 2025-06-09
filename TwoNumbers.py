"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1206/A -----------------------------------

You are given an array A, consisting of n positive integers a1,a2,…,an, and an array B, consisting of m positive integers b1,b2,…,bm.

Choose some element a of A and some element b of B such that a+b doesn't belong to A and doesn't belong to B.

For example, if A=[2,1,7] and B=[1,3,4], we can choose 1 from A and 4 from B, as number 5=1+4 doesn't belong to A and doesn't belong to B. 
However, we can't choose 2 from A and 1 from B, as 3=2+1 belongs to B.

It can be shown that such a pair exists. If there are multiple answers, print any.

Choose and print any such two numbers.

Input
The first line contains one integer n (1 ≤ n ≤ 100) — the number of elements of A.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 200) — the elements of A.

The third line contains one integer m (1 ≤ m ≤ 100) — the number of elements of B.

The fourth line contains m different integers b1,b2,…,bm (1 ≤ b(i) ≤ 200) — the elements of B.

It can be shown that the answer always exists.

Output
Output two numbers a and b such that a belongs to A, b belongs to B, but a+b doesn't belong to nor A neither B.

If there are multiple answers, print any.

Input:
1
20
2
10 20

Output:
20 20
"""
sze1 = int(input())
arrA = sorted(list(map(int, input().split())))
setA = set(arrA)
sze2 = int(input())
arrB = sorted(list(map(int, input().split())))
setB = set(arrB)
for i in range(sze1 - 1, -1, -1):
    numA = arrA[i]
    for j in range(sze2 - 1, -1, -1):
        numB = arrB[j]
        temp = numA + numB
        if(temp not in setA and temp not in setB):
            print(numA, numB)
            found = True
            break
    if(found):
        break
