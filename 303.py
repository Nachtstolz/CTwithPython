# P.303 # 내 방식 풀이 # 교재 참고 각각
# 4. 커리큘럼

# 동빈이는 온라인으로 컴퓨터공학 강의를 듣고 있다. 각 온라인 강의는 선수 강의가 있을 수 있고
# 선수 강의가 있는 강의는 선수 강의를 먼저 들어야 해당 강의를 들을 수 있다.
# 동빈이는 총 N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지 번호를 가진다.
# 동시에 여러 강의를 들을 수 있다고 가정하고, N=3일때, 3번 강의의 선수 강의로 1,2 강의가 있고
# 1,2 강의는 선수 강의가 없다고 가정하자. 그리고 각 강의 시간이 다음과 같다고 가정하자.
# 1번 강의 : 30시간 / 2번 강의 : 20시간 / 3번 강의 : 40시간
# 이 경우 1번 강의 수강까지 최소 시간 30시간, 2번 강의 수강까지 최소시간 20시간,
# 3번 강의 수강까지 최소 시간 70시간이다.
# 동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대해 수강하기까지 걸리는
# 최소 시간을 각각 출력하는 프로그램을 작성하시오.

# 첫째 줄에 동빈이 듣고자 하는 강의 수 N(1<=N<=500)이 주어진다.
# 다음 N개의 줄에는 각 강의의 강의 시간, 강의를 듣기 위해 먼저 들어야 하는 강의 번호가 자연수로 주어지며
# 각 자연수는 공백으로 구분한다. 이때 강의 시간은 100,000 이하의 자연수이다.
# 각 강의 번호는 1~N까지로 구성되며 각 줄은 -1로 끝난다.

# N개의 강의에 대해 수강하기까지 최소 시간을 한 줄에 하나씩 출력한다.

# 내 방식대로 풀이. DP Bottom up 느낌으로.
n = int(input())
arr = [0] * (n+1)
for i in range(1, n+1) :
    tmp = list(map(int, input().split()))
    #print(tmp, len(tmp))
    if len(tmp) == 2 : # 10 -1 의 경우 10 값 저장
        arr[i] = tmp[0]
        print(arr[i])
        continue

    maxi = 0
    for j in range(1, len(tmp)) :
        if tmp[j] == -1 : # -1이 나오면 값 저장 후 다음줄에서 또 입력받기
            arr[i] = maxi + tmp[0]
            continue
        maxi = max(maxi, arr[tmp[j]])    
    print(arr[i])


# 교재 풀이
# 위상 정렬 알고리즘
from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1) :
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1] : # 마지막 -1 인덱스까지
        indegree[i] += 1 # 거치는 간선의 개수 하나씩 증가
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort() :
    # 단순히 대입 연산을 했을 때 값 변경 문제가 발생할 수 있기에
    # 리스트 값을 복제해야 할 때는 deepcopy() 함수 사용
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    # 각 강의 수강까지 최소 시간 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1) :
        if indegree[i] == 0 :
            q.append(i)

    # 큐가 빌 때까지 반복
    while q :
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now] :
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0 :
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v+1) :
        print(result[i])

topology_sort()
