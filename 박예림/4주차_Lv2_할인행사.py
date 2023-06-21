# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    answer = 0
    want_n = []
    for n in range(len(number)):
        want_n += [want[n]] * number[n] # want의 물건들을 개수를 반영해 want_n에 저장
    
    for i in range(len(discount)-9):
        if sorted(want_n) == sorted(discount[i:10+i]): # want_n의 물건들과 discount의 열흘 간 물건들 내용이 일치한다면
            answer += 1

    return answer
