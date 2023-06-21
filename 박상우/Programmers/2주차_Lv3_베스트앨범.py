from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(int)
    find_dict = defaultdict(list)
    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        find_dict[genres[i]].append([i,plays[i]]) 
    for j, _ in sorted(genre_dict.items(), key=lambda x: x[1],reverse=True):
        if len(find_dict[j])==1:
            answer.append(find_dict[j][0][0])
        else:
            a=0
            for k in sorted(find_dict[j],key=lambda x: x[1],reverse=True):
                answer.append(k[0])
                a+=1
                if a > 1:
                    break
    return answer