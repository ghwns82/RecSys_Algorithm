# https://school.programmers.co.kr/learn/courses/30/lessons/159994
def solution(cards1, cards2, goal):
    make_goal = []
    for g in goal:
        if g in cards1:
            make_goal.append(cards1.pop(0))
        elif g in cards2:
            make_goal.append(cards2.pop(0))
                    
    if make_goal == goal: return "Yes"

    return "No"
