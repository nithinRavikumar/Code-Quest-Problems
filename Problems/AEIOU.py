# https://lmcodequestacademy.com/problem/aeiou

for _ in range (int(input())):
    s = input()
    print(sum(1 for char in s if char in 'aeiouAEIOU'))