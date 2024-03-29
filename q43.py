# P.397 # 그래프 이론 # 성공 # 크루스칼 알고리즘 기본 코드 참고
# Q43. 어두운 길

# 한 마을에 N개의 집과 M개의 도로가 구성되어 있다. 집은 0번부터 N-1번까지 번호로 구분된다.
# 모든 도로에 가로등이 구비되어 있는데, 도로의 가로등을 하루 켜기 위한 비용은 도로 길이와 같다.
# 정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의 두 집에 대해 가로등이 켜진 도로만으로도
# 오고 갈 수 있도록 만들고자 한다. 결과적으로 일부 가로등을 비활성화해 최대한 많은 금액을 절약하고자
# 한다. 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하라.

# 첫째 줄에 집의 수 N(1<=N<=200,000)과 도로의 수 M(N-1<=M<=200,000)이 주어진다.
# 다음 M개의 줄에 걸쳐 각 도로에 대한 정보 X, Y, Z가 주어지며 공백 구분한다.
# (0<=X,Y<N) 이는 X번 집과 Y번 집 사이 양방향 도로가 있고 그 길이가 Z라는 의미이다.
# 단, X와 Y가 동일한 경우는 없고 마을을 구성하는 모든 도로 길이의 합은 2의 31승보다 작다.

# 크루스칼 알고리즘 활용

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x) :
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
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

n, m = map(int, input().split())
parent = [0] * n # 부모 노드 저장할 배열 -> 부모 노드가 하나로 통일되면 종료
values = [] # 거리 값 저장할 배열
res = 0 # 최종 비용 저장할 변수
all_values = 0 # 모든 가로등을 설치했을 때 금액

for i in range(n) :
    parent[i] = i # 부모 노드 자기 자신으로 초기화 

for _ in range(m) :
    x, y, z = map(int, input().split())
    all_values += z
    values.append((z, x, y)) # 정렬하기 위해 비용을 맨 앞으로

values.sort() # 비용 순서로 정렬

for value in values :
    # 사이클이 생성하지 않는 경우 집합에 포함
    if find_parent(parent, value[1]) != find_parent(parent, value[2]) :
        union_parent(parent, value[1], value[2])
        res += value[0]

print(all_values - res)