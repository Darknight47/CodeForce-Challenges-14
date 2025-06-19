"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2117/A --------------------------------

Yousef is at the entrance of a long hallway with n doors in a row, numbered from 1 to n. He needs to
pass through all the doors from 1 to n in order of numbering and reach the exit (past door n).
Each door can be open or closed. If a door is open, Yousef passes through it in 1 second. If the door is closed, Yousef can’t pass through it.
However, Yousef has a special button which he can use at most once at any moment. This button makes all closed doors become open for x seconds.
Your task is to determine if Yousef can pass through all the doors if he can use the button at most once.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 1000) — the number of test cases.
The first line of each test case contains two integers n, x (1 ≤ n, x ≤ 10) — the number of
doors and the number of seconds of the button, respectively.
The second line of each test case contains n integers a1, a2, ..., an (ai ∈ {0, 1}) — the state of
each door. Open doors are represented by ’0’, while closed doors are represented by ’1’.
It is guaranteed that each test case contains at least one closed door.

Output
For each test case, output “YES” if Yousef can reach the exit, and “NO” otherwise.
You can output the answer in any case (upper or lower). For example, the strings “yEs”,
“yes”, “Yes”, and “YES” will be recognized as positive responses.

Input:
7
4 2
0 1 1 0
6 3
1 0 1 1 0 0
8 8
1 1 1 0 0 1 1 1
1 2
1
5 1
1 0 1 0 1
7 4
0 0 0 1 1 0 1
10 3
0 1 0 0 1 0 0 1 0 0

Output:
YES
NO
YES
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    used = False
    ok = True
    for i in range(n):
        door = arr[i]
        if(x <= 0 and used and door == 1):
            ok = False
            break
        elif(door == 1 and not used):
            used = True
            x -= 1
        elif(used):
            x -= 1
    print("YES" if ok else "NO")