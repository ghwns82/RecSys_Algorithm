import math
def solution(fees, records):
    answer = []
    parking = dict()
    
    for r in records:
        time = int(r[:2]) * 60 + int(r[3:5])
        car = r[6:10]
        status = r[11:]
        
        if car not in parking.keys():
            parking[car] = [time]
        else:
            parking[car].append(time)
    
    parking = sorted(parking.items())
    # print(parking[0][1])
    for p in parking:
        car = p[0]
        times = p[1]
        total = 0
        fee = 0
        if len(times) % 2 == 1: 
            times.append(23*60 + 59)
        
        for p in range(0, len(times), 2):
            total += (times[p+1] - times[p])
        
        if total < fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil((total-fees[0]) / fees[2]) * fees[3]
        answer.append(fee)
    
    return answer
