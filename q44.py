# P.398 # 그래프 이론 # 교재 참고 # 교재 코드 추가
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

''' 교재 아이디어 '''
# 임의의 두 노드 사이 터널을 연결할 수 있다고 가정하므로 간선의 개수는 N(N-1)/2.
# 최소 신장 트리를 만드는 문제 - 크루스칼 알고리즘. 시간 복잡도는 간선의 개수가 E라고 할 때 O(ElogE).
# 때문에  N이 최대 100,000이라는 입력 조건을 감안 -> 매우 큰 수가 될 수 있음. 모든 두 행성 간의 거리 확인 방법은 안됨.

# 하지만, 터널 비용이 min(|xa-xb|, |ya-yb|, |za-zb|)이기에 고려할 간선의 개수를 줄일 수 있다.
# 입력을 받은 뒤, x축, y축, z축을 기준으로 각각 정렬 수행.
# 예를 들어 문제에 나온 것과 같이 모든 행성의 좌표가 (11, -15, -15) (14, -5, -15) (-1, -1, -5) (10, -4, -1)
# (19, -4, 19)라고 하자. 이때 x축만 고려해서 정렬을 수행하면 -1, 10, 11, 14, 19가 된다.
# 결과적으로 각 행성의 x축에서의 거리는 차례대로 11, 1, 3, 5가 되는 것이다.
# 결과적으로 x축에 대해서만 4개의 간선만 고려하면 되는 것이다. 여기서 알아두어야 할 점은, 만약 y축 z축은 무시하고 오직 x축만
# 존재한다고 할때 이러한 4개의 간선만 이용해도 항상 최소 신장 트리를 만들 수 있다는 점이다.
# 즉, 이러한 방법을 이용하면 최소 신장 트리를 만들지 못하는 경우는 존재하지 않는다.
# 결과적으로 x축, y축, z축에 대해 정렬 이후 각각 N-1개의 간선만 고려해도 최적의 솔루션을 찾을 수 있다.
# 따라서 문제 풀이를 위해 고려한 총 간선의 개수는 3 x (N-1)개가 되고, 이를 활용해 크루스칼 알고리즘을 수행하면 제한시간 내 해결 가능하다.

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b


n = int(input())
parent = [0] * (n+1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1) :
    parent[i] = i

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for _ in range(1, n+1) :
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보 추출 처리
for i in range(n-1) :
    # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1])) # cost, a, b
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1])) # cost, a, b
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1])) # cost, a, b

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges :
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost

print(result)
    