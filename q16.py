# P.341 # 교재 참고
# Q16. 연구소
# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는
# 아직 퍼지지 않았고, 확산을 막기 위해 연구소에 벽을 세우려 한다.
# 연구소는 크기가 NxM인 직사각형으로 나타낼 수 있고 직사각형은 1x1 크기의 정사각형으로 나뉜다.
# 연구소는 빈 칸, 벽으로 이루어져 있고 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며 꼭 3개를 세워야 한다.
# 주어진 배열에서 0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳이다.
# 아무런 벽을 세우지 않으면 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하라.

# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3<=N,M<=8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈칸, 1은 벽, 2는 바이러스가 있는 위치다.
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈칸의 개수는 3개 이상이다.

# 최대한 2가 1로 감싸지도록 하는 방법
# 2와 1을 제외한 0의 개수를 구하면 된다 : 안전영역

''' 교재 풀이법 '''
# 벽의 개수가 3개가 되는 모든 조합을 찾은 후, 조합에 대해 안전 영역 크기 계산.
# 모든 조합 계산 시 파이썬의 조합 라이브러리 / DFS / BFS 사용.
# 안전 영역의 크기 계산 시 DFS / BFS 사용.

# DFS 혹은 BFS를 사용해 완전 탐색을 수행해야 함 -> DFS/BFS OR 완전 탐색 분류.
# 구현 과정이 까다롭기에 구현 유형으로도 분류 가능.

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n) :
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0 :
                # 해당 위치에 바이러스 배치하고, 다시 재귀적 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메소드
def get_score() :
    score = 0
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 0 :
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역 크기 계산
def dfs(count) :
    global res
    # 울타리가 3개 설치된 경우
    if count == 3 :
        for i in range(n) :
            for j in range(m) :
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        res = max(res, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n) :
        for j in range(m) :
            if data[i][j] == 0 :
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(res)    
        
