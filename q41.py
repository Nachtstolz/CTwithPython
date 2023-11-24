# P.393 # 그래프 이론 # 교재 참고
# Q41. 여행 계획

# 한울이가 사는 나라에는 N개의 여행지가 있고, 각 여행지는 1~N번까지 번호로 구분된다.
# 또한 임의의 여행지 사이 두 여행지를 연결하는 도로가 존재. 양방향 이동이 가능하다.
# 한울이는 하나의 여행 계획을 세운 뒤 이 여행 계획이 가능한지 여부를 판단하고자 한다.
# 여행지 개수와 여행지 간의 연결 정보가 주어졌을 때, 한울이의 여행 계획이 가능한지 여부를 판별하는
# 프로그램을 작성하라.
# 첫째 줄에 여행지 수 N과 여행 계획에 속한 도시 수 M이 주어진다.(1<=N,M<=500)
# 다음 N개의 줄에 걸쳐 NxN 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지 여부가 주어진다.
# 그 값이 1이라면 서로 연결되었다는 뜻이며, 0이라면 서로 연결되어 있지 않다는 의미이다.
# 마지막 줄에 한울이의 여행 계획에 포함된 여행지의 번호들이 주어지며 공백 구분한다.
# 한울이의 여행 계획이 가능하면 YES, 불가능하다면 NO를 출력한다.

INF = 1e8
n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]

parent = [0] * (n+1)
for i in range(1, n+1) :
    parent[i] = i

def find_parent(parent, x) :
    # 루트 노드가 아니라면 루트 노드까지 찾으러 가기
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

for i in range(1, n+1) :
    tmp = list(map(int, input().split()))
    for j in range(0, n) :
        arr[i][j+1] = tmp[j]

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if arr[i][j] == 1 :
            union_parent(parent, i, j)

plan = list(map(int, input().split()))

result = True
for i in range(m-1) :
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]) :
        result = False

if result == True :
    print('YES')
else :
    print('NO')