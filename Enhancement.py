"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1466/B --------------------------------------

Athenaeus has just finished creating his latest musical composition and will present it tomorrow to the people of Athens. 
Unfortunately, the melody is rather dull and highly likely won't be met with a warm reception.

His song consists of n notes, which we will treat as positive integers. The diversity of a song is the number of different notes it contains. 
As a patron of music, Euterpe watches over composers and guides them throughout the process of creating new melodies. She decided to help Athenaeus by changing his song to make it more diverse.

Being a minor goddess, she cannot arbitrarily change the song. Instead, for each of the n notes in the song, she can either leave it as it is or increase it by 1.

Given the song as a sequence of integers describing the notes, find out the maximal, achievable diversity.

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10000) — the number of test cases. Then t test cases follow, each one is described in two lines.

In the first line of each test case there is a single integer n (1 ≤ n ≤ 10^5) denoting the length of the song. 
The next line contains a sequence of n integers x1,x2,…,xn (1≤x1≤x2≤…≤xn≤2⋅n), describing the song.

The sum of n over all test cases does not exceed 10^5.

Output
For each test case, you should output a single line containing precisely one integer, the maximal diversity of the song, i.e. the maximal possible number of different 
elements in the final sequence.

Input:
5
6
1 2 2 2 5 6
2
4 4
6
1 1 3 4 4 5
1
1
6
1 1 1 2 2 2

Output:
5
2
6
1
3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    seen = set()
    
    for num in arr:
        if num in seen:
            seen.add(num + 1)  # If duplicate, attempt to increment
        else:
            seen.add(num)  # Otherwise, keep it
    
    print(len(seen))  # Count unique elements