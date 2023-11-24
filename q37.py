# P.385 # 최단 경로 # 성공
# Q37. 플로이드

# n(1<=n<=100)개의 도시가 있고, 한 도시에서 출발하여 다른 도시에 도착하는 m(1<=m<=100,000)개의
# 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다. 모든 도시의 쌍(A,B)에 대해 도시A에서 B로 가는 데
# 필요한 비용의 최솟값을 구하는 프로그램을 작성하라.
# 첫째 줄에 도시의 개수 n(1<=n<=100)이 주어진다. 둘째 줄에 버스의 개수 m(1<=m<=100,000)이 주어진다.
# 셋째 줄부터 m+2줄까지 다음과 같은 버스 정보가 주어진다. 먼저 처음에 버스 출발 도시의 번호가 주어진다.
# 버스 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다.
# 시작 도시와 도착 도시가 같은 경우는 없고 비용은 100,000보다 작거나 같은 자연수다.
# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
# n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 i->j로 가는데 필요한 최소비용이다.
# 만약, i->j로 갈 수 없다면 그 자리에 0을 출력한다.

INF = 1e8
n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            dist[a][b] = 0

for _ in range(m) :
    a, b, x = map(int, input().split())
    dist[a][b] = min(dist[a][b], x)

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if dist[i][j] == INF :
            print(0, end=' ')
        else :
            print(dist[i][j], end=' ')
    print()