# P.300 # 최소 신장 트리 # 교재 참고
# 3. 도시 분할 계획

# 동물원에서 막 탈출한 원숭이 한 마리가 세상 구경을 하고 있다. 어느 날 원숭이는 '평화로운 마을' 사람들이
# 도로 공사 문제로 머리를 맞대고 회의 중인 것을 보았다.
# 마을은 N개의 집과 집을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있다.
# 그리고 길마다의 유지 비용이 있다. 마을 이장은 마을을 2개의 분리된 마을로 분할 계획을 세우고 있는데,
# 마을 분할 시 분리된 마을 내 집들이 서로 연결되도록 분할해야 한다. 즉, 분리된 마을 내 두 집 사이 경로가 항상 존재햐아 한다.
# 마을에는 집이 하나 이상 있어야 한다.
# 그렇게 마을 이장은 계획을 세우다가 마을 내 길이 너무 많다는 생각을 했다. 일단, 분리된 두 마을 사이 있는 길은 필요가 없으므로
# 없앨 수 있고, 각 분리된 마을 내에서도 임의 두 집 사이 경로가 항상 존재하면서 길을 더 없앨 수 있다.
# 마을의 이장은 위 조건을 만족하도록 길을 모두 없애고 나머지 길의 유지비 합을 최소로 하고 싶다. 구하는 프로그램을 작성하라.

# 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2 이상 100,000 이하의 정수이고 M은 1 이상 1,000,000 이하 정수다.
# 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백 구분되어 주어지는데 A-B 연결 길의 유지비가 C(1<=C<=1,000)이다.
# 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.

def find_parent(parent, x) : # find(경로 압축형)
    if x != parent[x] :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) : # 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1) # 루트 노드 저장하는 배열
arr = [] # a, b, c값을 저장할 배열
res = 0 # 유지비 총합을 계산할 변수
long = 0 # 가장 비용이 큰 간선 유지비.
# 2개의 최소 신장 트리를 만들기 위해 최소 신장 트리 구성 간선 중 가장 비용이 큰 간선을 제거하기로.
# 교재 참고

for i in range(1, n+1) :
    parent[i] = i

for _ in range(m) :
    a, b, cost = map(int, input().split())
    arr.append((cost, a, b))

arr.sort() # cost 기준으로 배열 정렬

for i in arr :
    if find_parent(parent, i[1]) == find_parent(parent, i[2]) :
        continue
    union_parent(parent, i[1], i[2])
    res += i[0]
    long = i[0]


print(res - long)