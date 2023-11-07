# P.118 # 구현 # 수정 필요
# 3. 게임 개발

# 현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다.
# 캐릭터가 있는 장소는 1x1 크기의 정사각형으로 이뤄진 NxM 크기의 직사각형으로, 각각의 칸은 육지 / 바다이다.
# 캐릭터는 동서남북 중 한 곳을 바라본다.
# 맵의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수 B는 서쪽으로부터 떨어진 칸의 개수.
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
# 캐릭터의 움직임을 설정하기 위해 정해놓은 메뉴얼은 이러하다.

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전 -> 왼쪽 한 칸 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우에는
#    바라보는 방향을 유지한 채 한 칸 뒤로 가고 1단계롣 돌아간다.
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

# 위 과정을 반복 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
# 메뉴얼에 따라 캐릭터를 이동 -> 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

# 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다(3 <= N, M <= 50)
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분해 주어진다.
# 방향 d 값으로는 다음과 같이 4가지가 존재한다. (0: 북, 1:동, 2:남, 3:서)
# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다.
# N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
# 맵의 외곽은 항상 바다로 되어있다 (0:육지, 1:바다)
# 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.

# 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.

n, m = map(int, input().split(" ")) # 맵의 가로 세로 크기
x, y, d = map(int, input().split(" ")) # 사용자 위치와 방향
arr = []
for i in range(n) :
    arr1 = list(map(int, input().split(" "))) # 맵 내 육지와 바다 설정
    arr.append(arr1)
    #print(arr1) #arr1 생성 오류 여부 확인
#print(arr) #arr 생성 오류 여부 확인

check = [[0 for i in range(n)]for j in range(m)] # 가본 곳을 체크하기 위한 배열
check[x][y] = 1 # 첫 위치 방문
cnt = 1 # 첫 위치 방문
# 바라보는 방향 기준 좌측 접근
# 북(0) : (0, -1)
# 동(1) : (-1, 0)
# 남(2) : (0, 1)
# 서(3) : (1, 0)
move_x = [0, -1, 0, 1]
move_y = [-1, 0, 1, 0]
around = 0 # 네 방향 모두 가본 칸인지, 바다로 되어있는지 확인하는 변수
while True:
    if arr[x+move_x[d]][y+move_y[d]] == 0 and check[x+move_x[d]][y+move_y[d]] == 0:
        #print(x+move_x[d], y+move_y[d])
        check[x+move_x[d]][y+move_y[d]] = 1
        x+=move_x[d]
        y+=move_y[d]
        around = 0
        cnt+=1
        if d == 3 : # 서쪽 방향을 바라보고있을 때 왼쪽 방향 회전
            d = 0
        else : # 나머지 방향에서 왼쪽 방향 회전
            d+=1
        continue
    # 주행을 시도했으나 가지 못했을 경우
    check[x+move_x[d]][y+move_y[d]] = 1
    around+=1
    if around == 4 : # 네 방향 모두 가본 칸이거나 바다로 되어있을 때
        break
    if d == 3 : # 서쪽 방향을 바라보고있을 때 왼쪽 방향 회전
        d = 0
    else : # 나머지 방향에서 왼쪽 방향 회전
        d+=1
#print(check)
print(cnt)

''' 교재에서 제공하는 답안 '''
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)] # 리스트 컴프리헨션 문법
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True :
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[ny][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else :
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기 -> 내 코드에 반영 못했음. 수정 필요.
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        # 뒤로 바다가 막혀있는 경우
        else :
            break
        turn_time = 0

# 정답 출력
print(count)