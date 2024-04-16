# P.390 # 최단 경로 # 우선순위 큐 구현 일부 교재 참고
# Q40. 숨바꼭질

# 동빈이는 숨바꼭질을 하면서 술래로부터 잡히지 않도록 숨을 곳을 찾고 있다. 동빈이는 1~N번까지의 헛간 중에서 하나를 골라
# 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발한다. 전체 맴에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두
# 헛간을 연결한다. 또한 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어진다.
# 동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있다. 이때 최단 거리의 의미는 지나야 하는 길의
# 최소 개수를 의미한다. 동빈이가 숨을 헛간의 번호를 출력하라.

# 첫째 줄에는 N과 M이 주어지며, 공백으로 구분 (2<=N<=20,000), (1<=M<=50,000)
# 이후 M개의 줄에 걸쳐서 서로 연결된 두 헛간 A, B의 번호가 공백으로 구분되어 주어짐. (1<=A,B<=N)

# 첫 번째는 숨어야 하는 헛간 번호를(만약 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호를 출력)
# 두 번째는 그 헛간까지의 거리를, 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수 출력

# 뭔가 dfs / bfs로도 풀 수 있을 것 같다

import heapq

INF = int(1e9)
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)] # 연결 정보 담을 리스트
dist = [INF] * (n+1) # 최단 거리 저장 테이블

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start)) # 1 -> 1의 비용 0
    dist[start] = 0

    while q :
        long, now = heapq.heappop(q)
        #print(long, now)

        if dist[now] < long :
            continue
        
        for i in graph[now] :
            cost = long + i[1]
            if cost < dist[i[0]] :
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

''' 나의 출력 부분 구현 '''
hide_num = dist.index(max(dist[1:]))
max_dist = max(dist[1:])
hide_cnt = dist.count(max(dist[1:]))
print(hide_num, max_dist, hide_cnt)

''' 교재 출력 부분 구현 '''

'''
# 최단 거리가 가장 먼 노드 번호 (동빈이가 숨을 헛간의 번호)
max_node = 0
# 도달할 수 있는 노드 중, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 도일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n+1) :
    if max_distance < dist[i] :
        max_node = i
        max_distance = dist[i]
        result = [max_node]
    elif max_distance == dist[i] :
        result.append(i)

print(max_node, max_distance, len(result))
'''