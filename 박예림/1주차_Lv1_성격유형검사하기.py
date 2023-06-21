# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ''
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for s, c in zip(survey, choices):
        if c < 4: # 비동의 선택 시 
            scores[s[0]] += 4 - c # 첫 번째 캐릭터에 점수 부여
        elif c > 4: # 동의 선택 시
            scores[s[1]] += c - 4 # 두 번째 캐릭터에 점수 부여
    
    cat1 = list(scores.items())[::2] # 각 지표에서 첫 번째 유형 (R, C, J, A) (사전 순으로 더 빠름)
    cat2 = list(scores.items())[1::2] # 각 지표에서 두 번째 유형 (T, F, M, N)
    for c1, c2 in zip(cat1, cat2):
        if c1[1] >= c2[1]: # 첫 번째 유형 점수가 더 높거나 같은 경우
            answer += c1[0] # 첫 번째 유형 채택
        else: # 두 번째 유형 점수가 더 높은 경우
            answer += c2[0] # 두 번째 유형 채택
    return answer
  
