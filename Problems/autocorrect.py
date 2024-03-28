# https://lmcodequestacademy.com/problem/autocorrect

for _ in range(int(input())):
    d, w = map(int, input().split())
    dictionary = [input().strip() for _ in range(d)]
    words = [input().strip() for _ in range(w)]

    for word in words:
        min_distance = float('inf')
        closest = ''
        for dict_word in dictionary:
            if len(word) == len(dict_word):
                distance = sum(c1 != c2 for c1, c2 in zip(word, dict_word))
                if distance < min_distance:
                    min_distance = distance
                    closest = dict_word
        print(closest)
