# P.399 # 그래프 이론 # 교재 풀이
# Q45. 최종순위

# 올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다.
# 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다. 올해 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다.
# 그 대신에 작년에 비해서 상대적으로 순위가 바뀐 팀의 목록만 발표하려고 한다. (작년에는 순위를 발표했다)
# 예를 들어, 작년에 팀 13이 팀 6보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면 (6,13)을 발표할 것이다.
# 창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적 순위가 바뀐 모든 팀의 목록이 주어졌을 때,
# 올해 순위를 만드는 프로그램을 작성하라. 하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을
# 수도 있고, 일관성이 없는 잘못된 정보일 수도 있다. 이 두 경우 모두 찾아내야 한다.

# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다. 각 테스트 케이스는 다음과 같다.
#   - 팀의 수 n을 포함하고 있는 한 줄. (2<=n<=500)
#   - n개의 정수 ti를 포함하고 있는 한 줄. (1<=ti<=n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다.
#   모든 ti는 서로 다르다.
#   - 상대적인 등수가 바뀐 쌍의 수 m. (0<=m<=25000)
#   - 두 정수 ai와 b를 포함하고 있는 m줄. (1<=ai<bi<=n) 상대적인 등수가 바뀐 두 팀이 주어진다.
#   같은 쌍이 여러 번 발표되는 경우는 없다.

# 각 테스트 케이스에 대해 다음을 출력한다.
#   - n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다. 만약, 확실한 순위를 찾을 수
#   없다면 "?"를 출력한다. 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

''' 교재 풀이 '''
# '정해진 우선순위에 맞게 전체 팀들의 순서를 나열해야 한다'는 점 : 위상 정렬 알고리즘
# 작년의 순위 정보가 주어지면, '자기보다 낮은 등수를 가진 팀을 가리키도록' 방향 그래프를 만들 수 있다.
# ex) 팀은 5개 & 팀 5가 1등일 경우, 5번 노드가 1, 2, 3, 4를 모두 가리키도록

# 상대적인 순위가 바뀌게 되는 경우, 해당 간선의 방향을 반대로 변경. 
# ex) 팀 2와 팀 4 & 팀 3과 팀 4가 서로 순위가 바뀌면 팀2->팀4, 팀3->팀4이도록.

# 이후 이 상태에서 위상 정렬을 다시 수행한다.
# 위상 정렬은 2가지 특이 케이스가 존재한다. 1) 사이클이 발생하는 경우 2) 위상 정렬의 결과가 1개가 아닌 여러 가지인 경우
# 이 2가지 경우에 해당하지 않으면 위상 정렬을 수행한 결과는 '오직 하나의 경우'만 존재. 즉, 가능한 순위가 하나이다.
# 따라서 변경된 상대적 순위를 적용한 후, 위상 정렬 알고리즘을 실행하며 사이클이 발생하는지, 혹은 결과가 여러 가지인지 확인.
# 일반적인 위상 정렬의 경우, 정확히 N개의 노드가 큐에서 출력.
# 만약 노드가 N번 나오기 전에 큐가 비게 되면 : 사이클이 발생한 것으로 이해
# 특정 시점에 2개 이상의 노드가 큐에 한꺼번에 들어갈 때 : 가능한 정렬 결과가 여럭 가지
# -> 위상 정렬 수행 과정에서 큐에서 노드를 뽑을 때 큐의 원소가 항상 1개로 유지되는 경우에만 고유 순위 존재.

from collections import deque
# 테스트 케이스(Test Case)만큼 반복
for tc in range(int(input())) :
    # 노드 개수 입력 받기
    n = int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n+1) for i in range(n+1)]
    # 작년 순위 정보 입력
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n) :
        for j in range(i+1, n) :
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m) :
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b] : # a -> b로 연결되어있을 때
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else : # b -> a로 연결되어있을 때
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬(Topology Sort) 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)
    
    certain = True # 위상 정렬 결과가 오직 하나인지 여부
    cycle = False # 그래프 내 사이클 존재 여부

    # 정확히 노드 개수만큼 반복
    for i in range(n) :
        # 큐가 비어있다면 사이클이 발생했다는 의미
        if len(q) == 0 :
            cycle = True
            break

        # 큐의 원소가 두 개 이상이면 가능한 정렬 결과가 여러개라는 의미
        if len(q) >= 2 :
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n+1) :
            if graph[now][j] :
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0 :
                    q.append(j)

    # 사이클이 발생하는 경우 (일관성이 없는 경우)
    if cycle :
        print("IMPOSSIBLE")
    elif not certain :
        print("?")
    # 위상 정렬 수행 결과 출력
    else :
        for i in result :
            print(i, end = ' ')
        print()


''' 내 풀이 '''
# 위상 정렬 이용 # 순위별로 방향 생성
'''
from collections import deque

test = int(input()) # 테스트 케이스의 개수
while test > 0 :
    test-=1
    n = int(input()) # 팀의 수
    # 진입차수 저장 배열 및 -1으로 초기화
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    rank = list(map(int, input().split())) # 작년 성적 기준 랭킹 (0인덱스 : 1등)
    change = int(input()) # 순위 변화 개수
    
    # 작년 랭킹 기반으로 연결 및 진입차수 초기화
    for i in range(len(rank)-1) :
        graph[rank[i]].append(rank[i+1]) # 노드별 연결 정보
        indegree[rank[i]] +=1  # 진입차수 1씩 증가

    print(graph)
    print(indegree)

    for i in range(change) :
        a, b = map(int, input().split()) # 순위 변화 입력
        # 순위 변화에 따른 변화 시도 바로 가능. 벗 IMPOSSIBLE과 ?에 관한 예외처리 어떻게?
        # 두 개 이상의 같은 진입차수를 가지면 ?로 표현 가능할 것

        # IMPOSSIBLE과 ? 제외 처리 가능
        # tmp = indegree[a]
        # indegree[a] = indegree[b]
        # indegree[b] = tmp
        # 어떤 순서로, 어떻게 줘야할 지 고민중

    result = [] # 결과를 담을 리스트
    q = deque()

    # 처음 시작할 때 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)
    
    # 순위 변화 적용
    # 큐가 빌 때까지 반복
    while q :
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        print(now, result)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append(i)
 
    # 진입차수가 2인 것이 생긴다 -> ? 출력 -> 구현 어려움

    for i in result :
        print(i, end=' ')
    print()
'''
