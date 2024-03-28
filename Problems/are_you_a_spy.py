# https://lmcodequestacademy.com/problem/are-you-a-spy

for _ in range(int(input())):
    a, b = map(str, input().split("|"))
    clean = lambda s: ''.join(filter(str.isalpha, s.lower()))
    greeting, response = clean(a), clean(b)
    if all(char in greeting for char in response):
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")