from sys import stdin


def input():
    return stdin.readline().rstrip()

n,m = map(int,input().split())
pocketmon2idx = {}
idx2pocketmon = {}

for i in range(n):
    pocketmon = input()
    pocketmon2idx[pocketmon] = i+1
    idx2pocketmon[i+1] = pocketmon

for _ in range(m):
    question = input()
    if question.isdigit():
        print(idx2pocketmon[int(question)])
    else:
        print(pocketmon2idx[question])