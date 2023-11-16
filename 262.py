# P. 262 # 최단 경로 # 교재 참고 
# 3. 전보
# 어떤 나라에는 N개의 도시가 있고, 도시가 보내고자 하는 메시지가 있으면 다른 도시로 전보를 보내
# 다른 도시로 해당 메시지를 전송할 수 있다. 하지만, X -> Y 도시로 전보를 보내고자 하면 통로가
# 설치되어 있어야 한다. 예를 들어, X->Y 통로는 있지만 Y->X 통로가 없다면 Y->X 메시지 전송 X.
# 어느 날 C라는 도시에 위급 상황이 발생했고 최대한 많은 도시로 메시지를 보내고자 하는데,
# C 도시에서 출발해 각 도시 사이의 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것이다. 이때, 메시지를
# 받게 되는 도시의 개수는 총 몇 개이고 도시들이 메시지를 받는 데 걸리는 시간은 얼마인지 구해라.

# 첫째 줄에 도시 개수 N, 통로 개수 M, 메시지 보내고자 하는 도시 C가 주어진다.
# (1<=N<=30,000 1<=M<=200,000 1<=C<=N)
# 둘째 줄부터 M+1번째 줄에 걸쳐 통로에 대한 정보 X, Y, Z가 주어진다.
# 이는 도시 X -> Y 통로가 있고 전달 시간이 Z라는 의미다. (1<=X,Y<=N, 1<=Z<=1,000)
# 도시 C에서 보낸 메시지를 받는 도시 총 개수와 총 걸리는 시간을 공백 구분해 출력.

import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
# 노드별 연결된 즉, 우선순위 큐에 저장될 정보를 저장하는 리스트.
graph = [[] for i in range(n+1)]
# 최단 거리 테이블
dist = [INF] * (n+1)

for _ in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start) :
    queue = []
    heapq.heappush(queue, (0, start)) # 시작 노드로 가기 위한 최단 경로 0
    dist[start] = 0
    while queue :
        # 가장 최단 거리의 노드 추출
        distance, now = heapq.heappop(queue)
        if dist[now] < distance :
            continue
        for i in graph[now] :
            cost = distance + i[1] # i[0] : 목적지, i[1] : 거리
            if cost < dist[i[0]] :
                dist[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(c)

cnt = 0
maxi = 0
for i in dist :
    if i != INF :
        maxi = max(maxi, i)
        cnt+=1
print(cnt-1, maxi)