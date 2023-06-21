import sys

ins = []
for _ in range(int(sys.stdin.readline())):
    ins.append(sys.stdin.readline().rstrip())

ins = set(ins)
ins = list(ins)
ins.sort()
ins.sort(key=len)

print('\n'.join(ins))
