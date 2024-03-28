# https://lmcodequestacademy.com/problem/caught-speeding

for _ in range(int(input())):
    speed, bday = input().split()
    speed = int(speed)
    bday = bday == 'true'

    no_ticket = 65 if bday else 60
    small_ticket = 85 if bday else 80

    if speed <= no_ticket:
        print("no ticket")
    elif speed <= small_ticket:
        print("small ticket")
    else:
        print("big ticket")
