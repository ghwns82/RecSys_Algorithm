# idea
---
1. 앞에 번호만 상관이 있음 
2. 번호를 길이 순으로 정렬하고 짧은 번호 순대로 접두사가 되는 것이 있나 체크
3. 그리고 이미 확인한 짧은 번호는 필요가 없음
4. 먼저 길이가 같은 번호끼리 묶고
5. 길이가 1인 접두사 -> 2인 접두사 -> 3인 접두사 식으로 처리
6. 그리고 접두사를 명시해줘야함. 1113, 1113, 12, 이렇게 있을 때 1113일 때 걸려야하지만 12를 확인하는 과정에서 접두사가 무엇인지 명시하지 않으면 11이 겹쳐서 오답

테스트 1 〉	통과 (8.22ms, 12.5MB)    
테스트 2 〉	통과 (8.26ms, 12.3MB)    
테스트 3 〉	통과 (301.68ms, 78.3MB)    
테스트 4 〉	통과 (257.35ms, 69.8MB)    


# solution
---
```
from collections import defaultdict, deque
def solution(phone_book):
    answer = True
    phone_book = set(phone_book)
    dic = defaultdict(set)
    
    num_and_length = [(num, len(num)) for num in phone_book]    
    num_and_length.sort(key = lambda x: x[1])
    for num, length in num_and_length: 
        if num not in dic[length]: dic[length].add(num)
        else: return false
    
    for length in dic:
        count_dic = defaultdict(int)
        pre = dic[length]
        result, count_dic = check(count_dic, length, pre, pre)
        for n in pre: phone_book.discard(n)
        if result == False: return False
        
        result, count_dic = check(count_dic, length, phone_book, pre)
        if result == False: return False
        

    return True

def check(count_dic, length, nums, pre):
    for n in nums:
        count_dic[n[:length]] += 1
        
    for p in pre:
        if count_dic[p] > 1 : return False, count_dic
    
    return True, count_dic
