def solution(want, number, discount):
    answer = 0
    want_list = [i for i,n in zip(want,number) for _ in range(n)]
    day_num = len(discount)-10+1
    for j in range(day_num):
        if sorted(want_list)==sorted(discount[j:10+j]):
            answer+=1
    return answer