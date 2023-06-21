def solution(id_list, report, k):
    report_list = dict()
    for ids in id_list:
        report_list[ids] = [0]
        
    # 한 줄로 줄일 수 있음 . .
    # report_list = {x:0 for x in id_list}
    
    stop = list()
    for rep in report:
        u1, u2 = rep.split()
        if u2 not in report_list[u1]: 
            report_list[u1].append(u2)
            report_list[u2][0] += 1
            if u2 not in stop and report_list[u2][0] >= k:
                stop.append(u2)
    
    # 나는 report_list value에 u1이 신고한 u2를 넣어두었는데, 이 부분이 필요없을 듯
    # 동일한 신고내역은 1회로 처리하므로, set을 이용하여 중복 신고 버리기
    # 신고당한 유저 기준으로 dict 짜기
    
    # for rep in set(report):
    #     report_list[rep.split()[1]] += 1
        
    
    answer = [0 for i in range(len(id_list))]
    i = 0
    
    for k, v in report_list.items():
        for ids in v:
            if ids in stop:
                answer[i] += 1
        i += 1
        
    # for rep in set(report):
    #     if report_list[rep.split()[1]] >= k:
    #         answer[id_list.index(rep.split()[0])] += 1
            
    return answer
