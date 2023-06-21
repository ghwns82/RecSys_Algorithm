# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    q, r = divmod(s, n) # s를 n으로 나눈 몫, 나머지
    
    # s를 n으로 나눈 몫에 최대한 가까운 원소들로 구성해야, 모든 원소의 곱이 최대가 되는 원리를 이용
    if q == 0: # 몫이 없다면 집합을 만들 수 없음
        return [-1]
    
    elif r == 0: # 나머지가 0이면 해당 몫으로만 원소 구성
        return [q] * n
    
    else: # 나머지가 존재하면 나머지를 뺀 개수만큼만 몫으로 원소를 구성하고, 나머지 개수 만큼은 (몫+1) 값으로 원소 구성
        return [q] * (n - r) + [q + 1] * r 
