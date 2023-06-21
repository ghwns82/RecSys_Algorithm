n,m = map(int,input().split())
hear = []
see = []
for _ in range(n):
    hear.append(input())

for _ in range(m):
    see.append(input())
hear = set(hear)
see = set(see)
x = hear.intersection(see)
x = list(x)
x.sort()
print(len(x))
for i in x:
    print(i)