x, y, w, h = map(int, input().split())

# 동서남북
print(min([w-x, x, y, h-y]))
