# P.339 # 교재 참고 # 성공!
# Q15. 특정 거리의 도시 찾기

# 어떤 나라에는 1~N번까지의 도시와 M개의 단방향 도로가 존재. 모든 도로 거리는 1.
# 특정한 도시 X로부터 출발해 도달할 수 있는 모든 도시 중, 최단 거리가 정확히 K인 모든 도시 번호 출력
# 프로그램을 작성하시오. 출발 도시 X -> 출발도시 X 최단거리는 항상 0.

# 첫째 줄에 도시의 개수 N, 도로 개수 M, 거리 정보 K, 출발 도시 번호 X가 주어진다.
# (2<=N<=300,000, 1<=M<=1,000,000, 1<=K<=300,000 1<=X<=N)
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A,B가 주어지며 각 자연수는 공백으로 구분.
# 이는 A -> B 도시로 이동하는 단방향 도로가 존재한다는 의미(1<=A,B<=N). 단, A와 B는 서로 다른 자연수.
# X로부터 출발해 도달할 수 있는 도시 중 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순 출력,
# 도달할 수 있는 도시 중, 최단 거리가 K인 도시가 하나도 없으면 -1 출력.

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)] # 도로 즉, 간선 간 연결 저장
dist = [-1] * (n+1) # 출발지로부터 걸리는 거리 저장
dist[x] = 0 # 출발 도시 -> 출발 도시 거리는 0
queue = deque([x]) # 출발지 인덱스 우선 넣기

for _ in range(m) : # 도로 즉, 간선 정보 입력 받기
    a, b = map(int, input().split())
    graph[a] = b

''' 여기부터 교재 참고 '''
while queue : # 큐가 빌 때까지
    now = queue.popleft()
    for next in graph[now] :
        if dist[next] == -1 : # 방문한 적 없는 도시라면
            dist[next] = dist[now]+1
            queue.append(next)

# 최단 거리가 K인 모든 도시의 번호 오름차순 출력
check = False
for i in range(1, n+1) :
    if dist[i] == k :
        print(i)
        check = True
# 최단 거리가 K인 도시가 없다면 -1 출력
if check == False :
    print(-1)