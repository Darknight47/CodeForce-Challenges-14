"""
----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/294/A --------------------------------

Shaass has decided to hunt some birds. There are n horizontal electricity wires aligned parallel to each other. Wires are numbered 1 to n from top to bottom. 
On each wire there are some oskols sitting next to each other. Oskol is the name of a delicious kind of birds in Shaass's territory. Supposed there are ai oskols sitting on the i-th wire.

Sometimes Shaass shots one of the birds and the bird dies (suppose that this bird sat at the i-th wire). 
Consequently all the birds on the i-th wire to the left of the dead bird get scared and jump up on the wire number i - 1, if there exists no upper wire they fly away. 
Also all the birds to the right of the dead bird jump down on wire number i + 1, if there exists no such wire they fly away.

Shaass has shot m birds. You're given the initial number of birds on each wire, tell him how many birds are sitting on each wire after the shots.

Input
The first line of the input contains an integer n, (1 ≤ n ≤ 100). The next line contains a list of space-separated integers a1, a2, ..., an, (0 ≤ ai ≤ 100).

The third line contains an integer m, (0 ≤ m ≤ 100). Each of the next m lines contains two integers xi and yi. The integers mean that for the i-th time Shaass shoot the yi-th (from left) bird on the xi-th wire, 
(1 ≤ xi ≤ n, 1 ≤ yi). It's guaranteed there will be at least yi birds on the xi-th wire at that moment.

Output
On the i-th line of the output print the number of birds on the i-th wire.

Input:
5
10 10 10 10 10
5
2 5
3 13
2 12
1 13
4 6

Output:
0
12
5
0
16
"""
input()
wires = list(map(int, input().split()))
shots = int(input())
for i in range(shots):
    x, n = map(int, input().split())
    x -= 1
    wire = wires[x]
    leftBirds = n - 1
    rightBirds = wire - n
    if(x - 1 >= 0):
        wires[x - 1] += leftBirds
    wires[x] -= leftBirds
    if(x + 1 < len(wires)):
        wires[x + 1] += rightBirds
    wires[x] -= rightBirds
    wires[x] -= 1 
for num in wires:
    print(num)