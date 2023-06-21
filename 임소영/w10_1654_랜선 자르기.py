k, n = map(int, input().split())
kcm = list()
for i in range(k):
    kcm.append(int(input()))

start = 1
end = max(kcm)

while start <= end:
    temp = 0
    mid = (start + end) // 2

    for c in kcm:
        temp += c // mid
        
    if temp >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
