"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1592/A ------------------------------------------

One day, Ahmed_Hossam went to Hemose and said "Let's solve a gym contest!". Hemose didn't want to do that, as he was playing Valorant, so he came up with a problem and told it to Ahmed to distract him. 
Sadly, Ahmed can't solve it... Could you help him?

There is an Agent in Valorant, and he has n weapons. The i-th weapon has a damage value a(i), and the Agent will face an enemy whose health value is H.

The Agent will perform one or more moves until the enemy dies.

In one move, he will choose a weapon and decrease the enemy's health by its damage value. The enemy will die when his health will become less than or equal to 0. 
However, not everything is so easy: the Agent can't choose the same weapon for 2 times in a row.

What is the minimum number of times that the Agent will need to use the weapons to kill the enemy?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^5). Description of the test cases follows.

The first line of each test case contains two integers n and H (2 ≤ n ≤ 10^3 , 1 ≤ H ≤ 10^9) — the number of available weapons and the initial health value of the enemy.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the damage values of the weapons.

It's guaranteed that the sum of n over all test cases doesn't exceed 2⋅10^5.

Output
For each test case, print a single integer — the minimum number of times that the Agent will have to use the weapons to kill the enemy.

Input:
3
2 4
3 7
2 6
4 2
3 11
2 1 7

Output:
1
2
3
"""
cases = int(input())
for _ in range(cases):
    weapons, health = map(int, input().split())
    damages = sorted(list(map(int, input().split())))
    a = damages[weapons - 1]
    b = damages[weapons - 2]
    
    fullCycle = health // (a + b)
    remainingHealth = health % (a + b)

    if(remainingHealth == 0):
        print(fullCycle * 2)
    elif(remainingHealth <= a):
        print(fullCycle * 2 + 1)
    else:
        print(fullCycle * 2 + 2)