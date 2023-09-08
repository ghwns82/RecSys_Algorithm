# Idea
----
1. 문제를 이해하는데 오래결렸다. & 다른 사람들은 bit 연산? 가지고 푼 것 같지만 난 좀 복잡하게해서 구현하는데 어려움이 있었다.(리스트 크기 오류, 길이 안 맞음 등의 사소하게 신경써야할 부분이 많았음)
2. 푸는데 오래걸렸고 더 간단하고 간결한 논리로 푸는 연습을 해야할 듯
3. 기본적인 아이디어는 일단 이진수로 표현 -> but 이거는 left traversal로 트리를 탐색했을 때
4. 이진트리라면 root에서 bfs/dfs 했을 때 1의 개수가 2진수의 1개수와 같아야 한다.
5. 그래서 left traversal을 일반적인 tree index로 바꿔주고 dfs를 통해서 트리를 순회 -> 대신에 0이 있으면 끊겼다고 가정
6. 비교 후에 1/0 여부

# Code
----
```
### left traversal된 것을 차례대로 하도록 바꿔보자
### root가 1로 시작해 2345....
### lv이 4일 때는 traversal의 8번째가 root에 해당
### lv이 n일 때 1 3 5 ... 2^n-1 이 2^(n-1) ~ 2^n -1에 해당하고
###            2 6 2^n -2... 에 해당하는 거가 2^(n-2) ~ 2^(n-1) - 1 에 해당하니 매핑하자
### 그렇게 하면 트리가 복원되고 root에 시작해서 bfs/dfs 했을 때 1이 다 달 수 있어야함
#                8
#         4             12
#    2       6       10     14
#  1    3  5   7   9    11  13   15


def solution(numbers):
    result = []
    for n in numbers:
        
        min_lv = find_lv(n)
        ans = 0
        for lv in [min_lv, min_lv + 1]:
            tree, cnt = to_binary(n,lv)
            recovered_tree = recover_left_traversal(tree, lv)
            if cnt == bfs(recovered_tree):
                ans = 1
        result.append(ans)
    return result


def recover_left_traversal(tree, lv):
    
    recovered = [0 for _ in range(2**lv)] #root 1 부터
    
    for i in range(lv):
        step = 2**(i+1)
        left_start = 2**i
        left_end = 2**(lv) - 2**i
        
        tree_start = 2**(lv-i-1)
        tree_end = 2**(lv-i) - 1
        
        for left_idx, recover_idx in zip(range(left_start, left_end+step, step), range(tree_start, tree_end+1)):
            
            recovered[recover_idx] = tree[left_idx]

            
    return recovered


def to_binary(n, lv):
    idx = -1
    tmp = []
    while True:
        left = n % 2
        tmp.append(left)
        n = n//2
        idx -= 1
        if (n == 0) or (n == 1): 
            tmp.append(n)
            break 
    while len(tmp) !=  2**lv: tmp.append(0)
    return tmp[::-1], sum(tmp)
    

def find_lv(n):
    cum_sum = 0
    i = 0
    lv = 1
    while True:
        cum_sum += 2**i
        if n <= 2**cum_sum - 1: return lv 
        lv += 1
        i += 1
            
            
def bfs(tree):
    q = []
    if tree[1] == 1: q.append(1)
    cnt = 0
    while q:
        idx = q.pop()
        if tree[idx] == 1: cnt += 1
        
        l = idx *2
        r = idx*2 + 1
        
        if l < len(tree):
            if tree[l]==1:q.append(l)
        if r < len(tree):
            if tree[r]==1:q.append(r)
            
    return cnt
    
