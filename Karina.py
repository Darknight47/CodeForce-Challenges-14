"""
------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1822/B -----------------------------------

Karina has an array of n integers a1,a2,a3,…,an. 
She loves multiplying numbers, so she decided that the beauty of a pair of numbers is their product. And the beauty of an array is the maximum beauty of a pair of adjacent elements in the array.

For example, for n=4, a=[3,5,7,4], the beauty of the array is max (3⋅5, 5⋅7, 7⋅4) = max(15, 35, 28) = 35.

Karina wants her array to be as beautiful as possible. In order to achieve her goal, she can remove some elements (possibly zero) from the array. 
After Karina removes all elements she wants to, the array must contain at least two elements.

Unfortunately, Karina doesn't have enough time to do all her tasks, so she asks you to calculate the maximum beauty of the array that she can get by removing any number of elements (possibly zero).

Input
The first line of the input contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The description of the test cases follows.

The first line of a test case contains an integer n (2 ≤ n ≤ 2⋅10^5) — the length of the array a.

The second line of a test case contains n integers a1,a2,a3,…,an (−10^9 ≤ a(i) ≤ 10^9) — the elements of the array a.

The sum of all values of n across all test cases does not exceed 2⋅10^5.

Output
Output t integers, each of which is the answer to the corresponding test case — the maximum beauty of the array that Karina can get.

Input:
7
4
5 0 2 1
3
-1 1 0
5
2 0 -1 -4 0
6
-8 4 3 7 1 -9
6
0 3 -2 5 -4 -4
2
1000000000 910000000
7
-1 -7 -2 -5 -4 -6 -3

Output:
10
0
4
72
16
910000000000000000
42
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    temp1 = arr[0] * arr[1]
    temp2 = arr[sze - 1] * arr[sze - 2]
    print(max(temp1, temp2))