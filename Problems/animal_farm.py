# https://lmcodequestacademy.com/problem/animal-farm

for _ in range(int(input())):
    turkey, goat, horse = map(int, input().split())
    print(turkey * 2 + goat * 4 + horse * 4)