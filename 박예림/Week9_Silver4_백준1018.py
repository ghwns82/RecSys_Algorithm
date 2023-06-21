# 백준 1018번: 체스판 다시 칠하기 (https://www.acmicpc.net/problem/1018)

n, m = map(int, input().split())
board = [input() for _ in range(n)]

# 정답 board 생성 함수
def make_target_board(start_color, other_color):
  start_line = (start_color + other_color) * (m // 2) + (m % 2 == 1) * start_color
  other_line = (other_color + start_color) * (m // 2) + (m % 2 == 1) * other_color
  target_board = [start_line, other_line] * (n // 2) + (n % 2 == 1) * [start_line]
  return target_board

target_board_W = make_target_board('W', 'B') # W로 시작하는 정답 board
target_board_B = make_target_board('B', 'W') # B로 시작하는 정답 board

# 입력 받은 board의 각 line마다, target_board의 line과 비교해 색깔을 바꿔야 할 칸의 개수를 세는 함수
def diff_cnt_with_target_line(line, target_line):
  line_diff_cnt = 0
  for l, t in zip(line, target_line):
    line_diff_cnt += (l != t)
  return line_diff_cnt

# 만들어질 수 있는 모든 board의 경우에서, 다시 칠해야 할 칸 개수를 계산해 최소값을 찾아 출력
min_diff_cnt = 8 * 8
for i in range(n - 7):
  for j in range(m - 7):
    diff_cnt_with_target_board_W, diff_cnt_with_target_board_B = 0, 0
    for line_idx, line in enumerate([b[j:j+8] for b in board[i:i+8]]): # 만들어질 수 있는 8 * 8 보드의 한 case
      diff_cnt_with_target_board_W += diff_cnt_with_target_line(line, target_board_W[line_idx])  
      diff_cnt_with_target_board_B += diff_cnt_with_target_line(line, target_board_B[line_idx]) 
    
    if diff_cnt_with_target_board_W < diff_cnt_with_target_board_B:
      small_diff_cnt = diff_cnt_with_target_board_W
    else:
      small_diff_cnt = diff_cnt_with_target_board_B

    if small_diff_cnt < min_diff_cnt: 
      min_diff_cnt = small_diff_cnt

print(min_diff_cnt)
