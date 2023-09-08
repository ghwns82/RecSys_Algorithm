# Idea
----
## 내 아이디어
1. I의 인덱스만 추출해본다.
2. [2, 4, 6, 8, 9, 11, 12]. 
3. 3개니까 2에서 시작해서 확인 2 4 6 ok left = 6
4. head = 4로 이동
5. 3개 중에서 1개는 제외했으니까 다음 1개만 확인 (4 6) 8 ok = left 8
6. head = 6으로 이동
7. (6 8) 9 x -> 실패 지점 head = 9로 이동 = left = 9
8. 이전에 실패했으니 3개 다 확인 9 11 / 12 -> 실패 지점으로 이동 head 11

[3, 5, 7, 9, 10, 12, 13]
 0  1  2  3   4  5   6

3 5 7
left = 0
right = 1

1 & 0
2 & 1
3 right - left > window -> break

left = 1
right = 3(유지)

 5 7 9
 
 3 & 2 
 4 -> right - left > window -> break
 
 left = 2
 right = 4(유지)
 
 7 9 | 10
 
 4 & 3 -> X 
 
 left = right = 4
 right = left + 1
 
 
 10 12 | 13
 13

다만 시간복잡도 측면에서 O(n^2)의 복잡도. 통과는 하지만 O(n)으로 할 수 있는 방법을 찾아봤다.
연속된 IOI를 찾아서 한 번에 처리
1. 일단 IOI가 맞을 때까지 찾는다
2. 맞으면 cnt += 1 한다. & 현재까지 찾은 연속된 IOI 개수 = cnt가 N과 같으면 ans += 1
3. 그리고 cnt -= 1 해준다. IOIOIOI 같은 겨우 IOIOI가 매치되었다면 처음 IOI는 이제 제외해야하기 때문
4. index + 2를 해준다.
5. IOI가 아니면 cnt는 초기화(끊겼으니까)
6. 그리고 index는 +1 해준다.


 # Code
 ----
 ```
N = int(input())
M = int(input())

idxs = []
for idx, i in enumerate(input()):
    if i == 'I': idxs.append(idx)
        
left = 0
window = N
right = left + 1
result = 0
while right < len(idxs):
    
    success = True
    
    while success & (right - left <= window)&(right < len(idxs)):
        
        if idxs[right] - idxs[right-1] == 2:
            right += 1
        else:
            success = False
    
    if success & (right - left == window+1):
        left += 1
        result += 1
    else:
        left = right
        right = left + 1

print(result)


i = 0
ans = 0
cnt = 0
N = int(input())
M = int(input())
string = input()
while i < len(string) -2:
    
    if string[i:i+3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1
print(ans)
```

