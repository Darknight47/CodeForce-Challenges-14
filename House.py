"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/796/A -------------------------------------------

Zane the wizard had never loved anyone before, until he fell in love with a girl, whose name remains unknown to us.

The girl lives in house m of a village. There are n houses in that village, lining in a straight line from left to right: house 1, house 2, ..., house n. 
The village is also well-structured: house i and house i + 1 (1 ≤ i < n) are exactly 10 meters away. In this village, some houses are occupied, and some are not. Indeed, unoccupied houses can be purchased.

You will be given n integers a1, a2, ..., an that denote the availability and the prices of the houses. If house i is occupied, and therefore cannot be bought, then ai equals 0. 
Otherwise, house i can be bought, and ai represents the money required to buy it, in dollars.

As Zane has only k dollars to spare, it becomes a challenge for him to choose the house to purchase, so that he could live as near as possible to his crush. 
Help Zane determine the minimum distance from his crush's house to some house he can afford, to help him succeed in his love.

Input
The first line contains three integers n, m, and k (2 ≤ n ≤ 100, 1 ≤ m ≤ n, 1 ≤ k ≤ 100) — the number of houses in the village, the house where the girl lives, 
and the amount of money Zane has (in dollars), respectively.

The second line contains n integers a1, a2, ..., an (0 ≤ ai ≤ 100) — denoting the availability and the prices of the houses.

It is guaranteed that am = 0 and that it is possible to purchase some house with no more than k dollars.

Output
Print one integer — the minimum distance, in meters, from the house where the girl Zane likes lives to the house Zane can buy.

Input:
5 1 20
0 27 32 21 19

Output:
40
"""
n, m, k = map(int, input().split())
houses = list(map(int, input().split()))
girlHouse = m - 1
rightHouseIdx = -1
leftHouseIdx = -1
for i in range(girlHouse, n):
    tempHouse = houses[i]
    if(tempHouse > 0 and tempHouse <= k):
        rightHouseIdx = i
        break

for i in range(0, girlHouse + 1):
    th = houses[i]
    if(th > 0 and th <= k):
        leftHouseIdx = i

temp1, temp2 = 5000000, 5000000
if(rightHouseIdx != -1):
    diff = rightHouseIdx - girlHouse
    temp1 = diff * 10
if(leftHouseIdx != -1):
    diff2 = girlHouse - leftHouseIdx
    temp2 = diff2 * 10
print(min(temp1, temp2))