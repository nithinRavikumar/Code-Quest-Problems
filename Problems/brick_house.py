# https://lmcodequestacademy.com/problem/brick-house

for _ in range(int(input())):
    s, l, g = map(int, input().split())
    print("true" if g <= s + l * 5 and g % 5 <= s else "false")
