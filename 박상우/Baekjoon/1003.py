n = int(input())

for _ in range(n):
    i = int(input())
    a = 1
    b = 0 
    c = 0
    d = 1
    if i == 0:
        print(f"{a} {b}")
    elif i == 1:
        print(f"{c} {d}")
    else:
        for _ in range(i-1):
            a, b, c, d =c ,d, a+c, b+d
        print(f"{c} {d}")