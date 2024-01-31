# P.388 # 최단 경로
# Q39. 화성 탐사

# 당신은 화성 탐사 기계를 개발하는 프로그래머이다. 화성은 에너지 공급원을 찾기가 힘들다.
# 그래서 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때
# 항상 최적의 경로를 찾도록 개발해야 한다.
# 화성 탐사 기계가 존재하는 공간은 NxN 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 에너지 소모량이
# 존재한다. 가장 위쪽 칸인 [0][0] 위치에서 가장 오른쪽 아래 칸인 [N-1][N-1] 위치로 이동하는
# 최소 비용을 출력하는 프로그램을 작성하라. 기계는 특정한 위치에사 상하좌우로 1칸씩 이동 가능하다.

# 첫째 줄에 테스트 케이스의 수 T(1<=T<=10)가 주어진다.
# 매 테스트 케이스의 첫째 줄에 탐사 공간의 크기를 의미하는 정수 N이 주어진다. (2<=N<=125)
# 이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어지며 공백으로 구분한다(0<=각 칸의 비용<=9)
# 각 테스트 케이스마다 최소 비용을 한 줄에 하나씩 출력한다.

# 다익스트라 사용해서 우선순위 큐로 진행.
# 모든 노드들을 다 탐색할 것

import heapq
INF = 1e9
t = int(input()) # 테스트 케이스 수
# 상하좌우 이동을 위한 dx, dy
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

# 다익스트라 알고리즘 함수
def dijkstra(x, y, value) :
    queue = []
    # 첫번째 출발 값 넣어주기
    heapq.heappush(queue, (x, y, value))
    dist[x][y] = arr[x][y] # 첫 번째 거리 값 박기
    while queue : # 큐가 비어있지 않다면
        x, y, value = heapq.heappop(queue)
        # print('x, y, value : ', x, y, value) # 디버깅
        for i in range(4) : # 상하좌우 하나씩 가보기
            tx = x+dx[i]
            ty = y+dy[i]
            if 0 <= tx < n and 0 <= ty < n : # 배열 범위를 벗어나지 않을 때
                # dist[tx][ty]가 최소 거리로 갱신되었을 경우, 새로이 queue에 값 넣고 재확인하기
                dist_tmp = min(dist[x][y]+arr[tx][ty], dist[tx][ty])
                if dist_tmp != dist[tx][ty] :
                    dist[tx][ty] = dist_tmp
                    heapq.heappush(queue, (tx, ty, arr[tx][ty]))

# 테스트 케이스 횟수만큼 반복하기
while t > 0 :
    t-=1
    n = int(input()) # 탐사 공간의 크기
    arr = [] # 탐사 공간의 비용 저장할 배열
    dist = [[INF] * n for _ in range(n)] # 최단 거리 저장할 배열
    for _ in range(n) :
        tmp = list(map(int, input().split()))
        arr.append(tmp)
    dijkstra(0, 0, arr[0][0])
    # print(dist) # 디버깅
    print(dist[n-1][n-1])

