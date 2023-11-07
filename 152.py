# P.152 # DFS/BFS # 성공
# 책 내 소스코드 참고
# 4. 미로 탈출

# 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
# 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어집니다.
# 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
# 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

from collections import deque
n, m = map(int, input().split())
li = []
for i in range(n) :
    li.append(list(map(int, input())))
#print(li) # 입력 이상 없음 확인

# check = [[0 for j in range(m)] for i in range(n)] # 방문 여부 체크 리스트
queue = deque() # 큐 생성

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue.append((x, y))
    while queue : # queue가 빌 때까지
        x, y = queue.pop()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m : # out of index
                continue # dfs의 return 0 느낌
            # if check[nx][ny] == 1 : # 방문한 곳 제외
            #     continue # dfs의 return 0 느낌
            if li[nx][ny] == 0 : # 벽을 만났을 때
                continue # dfs의 return 0 느낌
            if li[nx][ny] == 1 :
                li[nx][ny] = li[x][y] + 1 # 책 속 그림 예제와 같이 만들기
                queue.append((nx, ny))

    # 가장 오른쪽 아래로 갔을 때의 값 (최소 경로) 추출
    return li[n-1][m-1]

print(bfs(0, 0))
            