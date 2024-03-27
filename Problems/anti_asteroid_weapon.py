# https://lmcodequestacademy.com/problem/anti-asteroid-weapon

from math import sqrt

n = int(input())
for _ in range(n):
    a = int(input())
    asteroids = [tuple(map(int, input().split())) for _ in range(a)]
    for x, y in sorted(asteroids, key=lambda p: sqrt(p[0]**2 + p[1]**2)):
        print(x, y)
