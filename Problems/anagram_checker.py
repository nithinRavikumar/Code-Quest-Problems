# https://lmcodequestacademy.com/problem/anagram-checker

for _ in range(int(input())):
    word1, word2 = input().split('|')
    word1_sorted = ''.join(sorted(word1))
    word2_sorted = ''.join(sorted(word2))
    if word1_sorted == word2_sorted and word1 != word2:
        print(word1+'|'+word2, '= ANAGRAM')
    else:
        print(word1+'|'+word2, '= NOT AN ANAGRAM')