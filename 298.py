# P.298 # 서로소 집합 알고리즘 # 성공
# 2. 팀 결성

# 학교에서 학생들에게 0~N번까지 번호를 부여했다. 처음에는 모든 학생이 서로 다른 팀으로
# 구분되어 N+1개의 팀이 존재하고, 이때 선생님은 '팀 합치기'와 '같은 팀 여부 확인'연산을 한다.
# 1. '팀 합치기' 연산은 두 팀을 합치는 연산이다.
# 2. '같은 팀 여부 확인' 연산은 특정 두 학생이 같은 팀에 속하는지 확인하는 연산이다.
# 선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인'연산에 대한 결과를 출력하는 프로그램을 작성하라.

# 첫째 줄에 N,M이 주어진다. M은 입력으로 주어지는 연산의 개수이다.(1<=N,M<=100,000)
# 다음 M개의 줄에는 각각의 연산이 주어진다.
# '팀 합치기' 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다.
# '같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속하는지 확인한다.
# a와 b는 N 이하의 양의 정수이다.
# '같은 팀 여부 확인' 연산에 대해 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.

n, m = map(int, input().split())
#arr = [] # 연산이 들어가는 줄. 튜플 형태로 넣을 예정.
parent = [0] * (n+1)

for i in range(n+1) :
    parent[i] = i # 루트 노드를 본인으로 설정

def find_parent(parent, x) : # find(경로 압축)
    if x != parent[x] :
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) : # 팀 합치기 연산
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b : 
        parent[b] = parent[a]
    else :
        parent[a] = parent[b]

for _ in range(m) :
    number, a, b = map(int, input().split())
    if number == 0 :
        if find_parent(parent, a) == find_parent(parent, b) :
            union_parent(parent, a, b)
    elif number == 1 :
        if parent[a] == parent[b] :
            print("YES")
        else :
            print("NO")
