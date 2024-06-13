# P.351 # DFS/BFS # 교재 참고 + 내 풀이 혼합
# Q20. 감시 피하기

# NxN 크기의 복도가 있따. 이 복도는 1x1 크기의 칸으로 나누어지며 특정 위치에 선생님, 학생, 혹은 장애물이 있다.
# 현재 학생 몇 명이 수업 시간에 몰래 복도에 나왔는데, 복도에 나온 학생들이 선생님의 감시에 들키지 않는 것이 목표이다.
# 각 선생님은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시한다. 단, 복도에 장애물이 있으면 선생님은 장애물 뒤편에 숨은
# 학생을 볼 수 없다. 선생님은 시력이 매우 좋아 아무리 멀리 있더라도 장애물로 막히기 전까지 4가지 방향으로 학생을 볼 수 있다.
# 문제에서 위칫값을 나타낼 때는 (행, 열)의 형태로 표현한다. 각 칸은 선생님이 존재하면 T, 학생이 존재하면 S,
# 장애물이 존재하면 O로 표시한다. 

# 예시) 복도가 3x3 크기일 때 (3,1)에는 선생님이 존재하며 (1,1), (2,1), (3,3)의 위치에는 학생이 존재한다.
# 그리고 (1,2), (2,2), (3,2)의 위치에는 장애물이 존재한다.
# 이때, (3,3)의 위치에 존재하는 학생은 장애물 뒤편에 숨어있기 때문에 감시를 피할 수 있지만, (1,1)과 (2,1)의 위치에
# 존재하는 학생은 선생님에게 들킨다.
# 학생들은 복도의 빈칸 중 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 한다. 그리고 장애물 3개를 설치해서
# 선생님의 감시로부터 모든 학생이 피할 수 있는지 계산해야 한다. NxN 크기의 복도에서 학생과 선생님의 위치 정보가 주어졌을 때,
# 장애물을 정확히 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력하는 프로그램을 작성하라.

# 첫째 줄에 자연수 N이 주어진다. (3<=N<=6)
# 둘째 줄에 N개의 줄에 걸쳐 복도의 정보가 주어진다. 각 행에서는 N개의 원소가 주어지며, 공백으로 구분한다. 해당 위치에
# 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다. 단, 항상 빈칸의 개수는 3개 이상이다.

# 첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다.
# 모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력한다.

''' 교재 풀이 개념 '''
# 장애물을 정확히 3개 설치하는 모든 경우 확인, 매 경우마다 모든 학생을 감시로부터 피하도록 할 수 있는지 여부 출력
# 장애물을 정확히 3개 설치하는 모든 경우의 수 = 복도의 크기 N이 최대 6이기에 모든 조합의 수는 최악의 경우 36C3
# -> 10,000 이하의 수이므로 모든 조합을 고려해 완전 탐색 수행해도 시간 초과 없이 문제 해결 가능
# 1. 모든 조합을 찾기 위해 DFS / BFS를 이용해 조합 반환 함수 작성 2. 파이썬 조합 라이브러리 사용 방식으로 해결 가능

# 정확히 3개의 장애물이 설치된 모든 조합마다, 선생님들의 위치 좌표 확인 -> 각각 선생님 위치에서 상, 하, 좌, 우 확인
# 학생이 한 명이라도 감지되는지 확인하는 별도 메소드 구현하면 편리.

''' 교재 풀이 '''
from itertools import combinations

n = int(input())
board = [] # 복도 정보(N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n) :
    board.append(list(input().split()))
    for j in range(n) :
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T' :
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X' :
            spaces.append((i, j))

# 특정 방향으로 감시 진행 (학생 발견 : True, 미발견 : False)
def watch(x, y, direction) :
    # 왼쪽 방향으로 감시
    if direction == 0 :
        while y >= 0 :
            if board[x][y] == 'S' : # 학생이 있는 경우
                return True
            if board[x][y] == 'O' : # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1 :
        while y < n :
            if board[x][y] == 'S' : # 학생이 있는 경우
                return True
            if board[x][y] == 'O' : # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2 :
        while x >= 0 :
            if board[x][y] == 'S' : # 학생이 있는 경우
                return True
            if board[x][y] == 'O' : # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3 :
        while x < n :
            if board[x][y] == 'S' : # 학생이 있는 경우
                return True
            if board[x][y] == 'O' : # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process() :
    # 모든 선생님의 위치 하나씩 확인
    for x, y in teachers : 
        # 4가지 방향으로 학생 감지할 수 있는지 확인
        for i in range(4) :
            if watch(x, y, i) :
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

# 빈 공간에서 3개를 뽑는 모든 조합 확인
for data in combinations(spaces, 3) :
    # 장애물 설치해보기
    for x, y in data :
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process() :
        # 원하는 경우 발견
        find = True
        break
    # 설치된 장애물 다시 없애기
    for x, y in data :
        board[x][y] = 'X'

if find :
    print('YES')
else :
    print('NO')

''' 개념 활용 나의 풀이 '''
# 선생님 입장에서 학생 탐지하는 공식은 교재 풀이 약간 참고
'''
n = int(input())
graph = [] # 복도 정보
empty = [] # 빈 공간의 좌표값 저장할 배열
comb = [] # 빈 공간 기반으로 3개의 장애물 좌표 조합 저장할 배열
teachers = [] # 선생님 좌표 저장

# 입력 받아서 복도 정보 정리하기
# 선생님(T) : 1, 학생(S) : 2, 빈 공간(X) : 0, 장애물(O) : -1
for i in range(n) :
    tmp = list(input().split())
    tmp2 = []
    int_j = 0
    for j in tmp :
        if j == 'T' :
            tmp2.append(1)
            teachers.append((i, int_j))
        elif j == 'S' :
            tmp2.append(2)
        elif j == 'X' :
            tmp2.append(0)
            empty.append((i, int_j))
        int_j+=1
    graph.append(tmp2) 

# print(empty) 

# DFS 사용하여 조합 찾기 # 인터넷 약간 참고
# (a,b) 형태의 원소를 저장해야

def dfs(depth, stack=[], result=[]) :
    if len(stack) == 3 : # 무조건 장애물 3개 설치
        result.append(stack.copy())
        return
    
    for i in range(depth, len(empty)) :
        stack.append((empty[i]))
        dfs(i+1, stack, result)
        stack.pop()
    
    return result

comb = dfs(0)
# print(len(comb)) # 조합 수 비교하기 -> 잘 뽑았는지 확인용
# print(res)

# 감시했을 때 학생 발견 및 미발견 확인
def check(x, y, direction) :
    # x, y = 선생님 x, y 좌표

    # 왼쪽
    if direction == 0 and y > 0 :
        dy = y-1
        while dy >= 0 :
            if graph[x][dy] == -1 : # 장애물이 있는 경우
                return False
            if graph[x][dy] == 2 : # 학생이 있는 경우
                return True
            dy-=1
    # 오른쪽 
    if direction == 1 and y < n-1 :
        dy = y+1
        while dy < n :
            if graph[x][dy] == -1 : # 장애물이 있는 경우
                return False
            if graph[x][dy] == 2 : # 학생이 있는 경우
                return True
            dy+=1
    # 위
    if direction == 2 and x > 0 :
        dx = x-1
        while dx >= 0 :
            if graph[dx][y] == -1 : # 장애물이 있는 경우
                return False
            if graph[dx][y] == 2 : # 학생이 있는 경우
                return True
            dx-=1
    # 아래
    if direction == 3 and x < n-1 :
        dx = x+1
        while dx < n :
            if graph[dx][y] == -1 : # 장애물이 있는 경우
                return False
            if graph[dx][y] == 2 : # 학생이 있는 경우
                return True
            dx+=1
    return False # 사람도 장애물도 만나지 않을 경우

# 장애물 설치 시 학생 한 명이라도 감지 여부 검사
def process() : 
    # 모든 선생님의 위치 하나씩 확인
    for x, y in teachers :
        for i in range(4) :
            if check(x, y, i) :
                return True # 하나라도 true가 반환되면 true
    return False

find = False # 학생이 한 명도 감지되지 않는다는 전제로 시작

# 각 조합마다 장애물 설치 - 감시했을 때 학생 감지 여부 검사
for each in comb :
    # 장애물 설치하기
    for i in each :
        x, y = i
        graph[x][y] = -1
    # 학생이 한 명도 감지되지 않으면
    if not process() :
        find = True
        break
    # 장애물 제거하기
    for i in each :
        x, y = i
        graph[x][y] = 0

if find :
    print('YES')
else :
    print('NO')

'''


