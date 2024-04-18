# P.327 # 구현 # 성공
# Q11. 뱀

# 'Dummy'라는 도스 게임이 있다. 이 게임에는 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
# 뱀이 이리저리 기어다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다.
# 게임은 NxN 정사각 보드 위 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에는 벽이 있다.
# 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1이다. 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다. -> 머리가 늘어난다
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하시오.

# 첫째 줄에 보드의 크기 N이 주어진다(2<=N<=100). 다음 줄에 사과의 개수 K가 주어진다(0<=K<=100).
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측(1행 1열)에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L이 주어진다(1<=L<=100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며, 게임 시작 시간으로부터
# X초가 끝난 뒤에 왼쪽(C가 'L) 또는 오른쪽(C가 'D')으로 90도 방향을 회전시킨다는 뜻이다.
# X는 10,000 이하의 양의 정수이며, 방향 변환 정보는 X가 증가하는 순으로 주어진다.

from collections import deque

q = deque()
n = int(input()) # 보드 크기 
k = int(input()) # 사과 개수
arr = [[0] * n for _ in range(n)]
# apple = [] # 사과 위치 저장
direction = [] # 방향 변환 정보
for i in range(k) :
    x, y = map(int, input().split())
    arr[x-1][y-1] = 2 # 사과는 2로 표시
    # apple.append((x, y))
l = int(input()) # 뱀의 방향 변환 횟수
for i in range(l) :
    time, dir = input().split()
    direction.append((int(time), dir))
# print(apple)
# print(direction)
# print(arr)

# 0인덱스 : 기존 우측 직진. 우회전 기준 (D) 순방향 = 좌회전 기준(L) 역방향
x_turn = [0, 1, 0, -1]
y_turn = [1, 0, -1, 0]
arr[0][0] = 1 # 첫 시작 1로 표시

second = 0
head_x = 0
head_y = 0
idx = 0 # 회전 리스트 인덱스
q.append((0,0))
while True :
    second += 1
    # 사전) 회전 여부 확인 - 맞게 직진 방향 변경
    if len(direction) != 0 :
        time, dir = direction[0]
        if second-1 == time :
            direction.pop(0)
            if dir == 'D' :
                idx+=1
            else :
                idx-=1
            
            if idx < 0 :
                idx = 3

    # 벽에 부딪혔는지 확인 -> break
    head_x = head_x + x_turn[idx]
    head_y = head_y + y_turn[idx]
    if head_x < 0 or head_x >= n or head_y < 0 or head_y >= n :
        break

    # 내 몸에 부딪혔는지 확인 -> break
    if arr[head_x][head_y] == 1 :
        break

    # 이동하기
    if arr[head_x][head_y] == 0 : # 사과가 없을 때
        tail_x, tail_y = q.popleft()
        arr[tail_x][tail_y] = 0
    q.append((head_x, head_y))
    arr[head_x][head_y] = 1

print(second)
    