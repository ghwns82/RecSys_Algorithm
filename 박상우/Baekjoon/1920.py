n = int(input())
A = list(map(int,input().split()))
m = int(input())
X = list(map(int,input().split()))

A = set(A)

for i in X:
    if i in A:
        print(1)
    else:
        print(0)