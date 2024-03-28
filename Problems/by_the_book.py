# https://lmcodequestacademy.com/problem/by-the-book

for _ in range(int(input())):
    isbn = input()
    S = sum((10 - i) * (10 if x == 'X' else int(x)) for i, x in enumerate(isbn))
    print("VALID" if S % 11 == 0 else "INVALID")
