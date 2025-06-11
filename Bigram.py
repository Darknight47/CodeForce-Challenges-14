"""
-------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1618/B --------------------------

Polycarp has come up with a new game to play with you. He calls it "A missing bigram".

A bigram of a word is a sequence of two adjacent letters in it.

For example, word "abbaaba" contains bigrams "ab", "bb", "ba", "aa", "ab" and "ba".

The game goes as follows. First, Polycarp comes up with a word, consisting only of lowercase letters 'a' and 'b'. 
Then, he writes down all its bigrams on a whiteboard in the same order as they appear in the word. After that, he wipes one of them off the whiteboard.

Finally, Polycarp invites you to guess what the word that he has come up with was.

Your goal is to find any word such that it's possible to write down all its bigrams and remove one of them, so that the resulting sequence of bigrams is the same as the one Polycarp ended up with.

The tests are generated in such a way that the answer exists. If there are multiple answers, you can print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 2000) — the number of testcases.

The first line of each testcase contains a single integer n (3 ≤ n ≤ 100) — the length of the word Polycarp has come up with.

The second line of each testcase contains n−2 bigrams of that word, separated by a single space. Each bigram consists of two letters, each of them is either 'a' or 'b'.

Additional constraint on the input: there exists at least one string such that it is possible to write down all its bigrams, except one, so that the resulting sequence 
is the same as the sequence in the input. In other words, the answer exists.

Output
For each testcase print a word, consisting of n letters, each of them should be either 'a' or 'b'. 
It should be possible to write down all its bigrams and remove one of them, so that the resulting sequence of bigrams is the same as the one Polycarp ended up with.

The tests are generated in such a way that the answer exists. If there are multiple answers, you can print any of them.

Input:
4
7
ab bb ba aa ba
7
ab ba aa ab ba
3
aa
5
bb ab bb

Output:
abbaaba
abaabaa
baa
bbabb
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    bigrams = list(input().split())
    word = bigrams[0]  # Start with the first bigram
    for i in range(1, n - 2):
        if word[-1] == bigrams[i][0]:  
            # If last character matches first character of next bigram, append second letter
            word += bigrams[i][1]
        else:
            # If there’s a mismatch, insert the missing character (from the next bigram)
            word += bigrams[i][0] + bigrams[i][1]

    # If length is short, append 'a' or 'b' to meet the expected size
    while len(word) < n:
        word += 'a'
    print(word)    