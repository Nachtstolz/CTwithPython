# P.110 # 구현
# 예제 4-1. 상하좌우

# 여행가 A는 N X N 크기의 정사각형 공간 위에 서있다.
# 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.
# L : 왼쪽 한 칸 이동 R : 오른쪽 한 칸 이동 U : 위 한 칸 이동 D : 아래 한 칸 이동
# 이 때, 여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
# 예를 들어 (1,1)의 위치에서 L 혹은 U를 만나면 무시된다.
# 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<=N<=100)
# 둘째 줄에 여행가 A가가 이동할 계획서 내용이 주어진다. (1<=이동 횟수<=100)
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.

n = int(input())
str = list(input().split(" "))
# print(n, str) # 디버깅

x = y = 1
for i in str :
    if i == 'L' :
        if y<=1 :
            continue
        y-=1
    elif i == 'R' :
        if y>=n :
            continue
        y+=1
    elif i == 'U' :
        if x<=1 :
            continue
        x-=1
    elif i == 'D' :
        if x>=n :
            continue
        x+=1
print(x, y)


'''보다 쉬운 문제 해결 방법 (교재 참고)'''
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D'] # move_types[i] = dx[i]+dy[i]

# 이동 계획을 하나씩 확인
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)