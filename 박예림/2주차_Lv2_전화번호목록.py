# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    p_dict = {}
    for p in phone_book:
        if p in p_dict:
            return False
        else:
            for k in p_dict.keys():
                if len(p) < len(k):
                    sht = p
                    lng = k
                else:
                    sht = k
                    lng = p
                    
                if lng[:len(sht)] == sht: # 시간 초과..
                    return False
            p_dict[p] = 1
            
    return True
