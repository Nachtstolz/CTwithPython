# P.398 # 그래프 이론 # 교재 참고
# Q44. 행성 터널

# 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다.
# 민혁이는 이 행성을 효율적으로 지배하기 위해 행성을 연결하는 터널을 만드려고 한다.
# 행성은 3차원 좌표 위의 한 점으로 생각하면 된다. 두 행성 A(xa, xy, xz)와 B(xb, yb, zb)를 터널로
# 연결할 때 드는 비용은 min(|xa-xb|, |ya-yb|, |za-zb|)이다.
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때 모든 행성을 터널로 연결하는데 필요한
# 최소 비용을 구하는 프로그램을 작성하라

# 첫째 줄에 행성의 개수 N이 주어진다(1<=N<=100,000)
# 다음 N개의 줄에 각 행성의 x, y, z 좌표가 주어진다
# 모든 좌표 값은 -10의 9승보다 크거나 같고, 10의 9승보다 작거나 같은 정수이다.
# 한 위치에 행성이 두 개 이상인 경우는 없다.
# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.


# 모두를 하나의 선으로 연결하는 + 싸이클이 생기지 않는 그래프 -> 신장트리

def find_parent(x, parent) :
    if parent[x] != x :
        parent[x] = find_parent(parent[x], parent)
    return parent[x]
    

def union_parent(a, b) :
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    
INF = int(1e9)
n = int(input())
graph = [] # 위치 정보 저장
dist = [[] * n for _ in range(n)]
edges = [] # (cost, a, b) 저장
parent = [INF] * n # 연결 부모 노드 저장
result = 0

for i in range(n) :
    x, y, z = map(int, input().split())
    graph.append((x,y,z))
    parent[i] = i # 부모 노드 초기화

for i in range(n) : # 터널 연결 비용 계산 및 저장
    for j in range(i+1, n) :
        tmp1 = abs(graph[i][0] - graph[j][0])
        tmp2 = abs(graph[i][1] - graph[j][1])
        tmp3 = abs(graph[i][2] - graph[j][2])
        #dist[i][j] = dist[j][i] = min(tmp1, tmp2, tmp3)
        # 무조건 i < j
        edges.append((min(tmp1, tmp2, tmp3), i, j))

edges.sort() # 비용이 작은 순서대로 정렬
#print(edges)

for edge in edges :
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우
    if find_parent(a, parent) != find_parent(b, parent) :
        union_parent(a, b)
        result+=cost

print(result)

