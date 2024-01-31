# P.388 # 최단 경로 # 성공 # 교재 참고
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

''' 교재 풀이 방법 '''
# NxN 크기의 맵이 주어졌을 때, 맵의 각 위치(칸)를 노드로 보고 상하좌우로 모든 노드가 연결되어 있다고 보면 된다.
# 예를 들어, 위치 A, B가 서로 인접해있다고 할 때, A->B 비용은 B위치의 탐사 비용, B->A 비용은 A위치의 탐사 비용이 된다.
# N의 범위 크기가 최대 125로 작게 느껴질 수도 있지만 2차원 공간이기에 전체 노드의 개수는 N제곱으로 10,000을 넘을 수 있다.
# 따라서 플로이드 워셜 알고리즘으로는 이 문제를 해결하기에 적합하지 않으므로 다익스트라 최단 경로 알고리즘으로
# 답을 도출할 수 있다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 테스트 케이스만큼 반복
for tc in range(int(input())) :
    # 노드의 개수 입력받기
    n = int(input())
    # 전체 맵 정보 입력받기
    graph = []
    for i in range(n) :
        graph.append(list(map(int, input().split())))

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0 # 시작 위치는 (0,0)
    # 시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘 수행
    while q :
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 처리된 적이 없다면 distance[x][y] = INF 이기 때문에 항상 큼
        if distance[x][y] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny] :
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])
