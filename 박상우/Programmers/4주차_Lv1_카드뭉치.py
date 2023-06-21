def solution(cards1, cards2, goal):
    for i in goal:
        if cards1:
            if i == cards1[0]:
                cards1.pop(0)
                continue
        if cards2:
            if i == cards2[0]:
                cards2.pop(0)
            else:
                return "No"
        else:
            return "No"
    return "Yes"