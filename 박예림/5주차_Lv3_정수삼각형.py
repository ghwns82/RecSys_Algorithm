# [프로그래머스] DP - Lv 3. 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# reference : https://codedrive.tistory.com/49
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):  # i+1 = len(triangle[i])
            if j == 0: # 각 줄에서 첫 번째 숫자
                triangle[i][j] += triangle[i-1][j]
            elif j == i: # 각 줄에서 마지막 숫자
                triangle[i][j] += triangle[i-1][j-1]
            else: # 각 줄에서 중간 숫자들
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])
