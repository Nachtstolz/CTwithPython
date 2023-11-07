# P.149 # DFS/BFS # 성공
# DFS 사용 문제임을 확인 + 약간의 코드 참조 후 풀이 완료
# 3. 음료수 얼려 먹기

# N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.(1 <= N, M <= 1000)
# 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

n, m = map(int, input().split())
li = []
for i in range(n) :
    li.append(list(map(int, input())))
    #바로 li에 저장할 수 있도록 변경
    #li.append(tmp)
    #print(tmp)
check = [[0 for j in range(m)] for i in range(n)]
def dfs(x,y) :
    if x <= -1 or x >= n or y <= -1 or y >= m : # 범위를 벗어났으면 빠져나오기
        return 0
    if check[x][y] == 1 : # 경유한 곳이면 빠져나오기
        return 0
    if li[x][y] == 0 :
        check[x][y] = 1 # 경유 체크
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return 1

cnt = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == 1 :
            cnt+=1

print(cnt)

''' 책 내부 코드 필사 '''
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y) :
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        # 해당 노드 방문 처리 
        graph[x][y] = 1 # 💡 주어진 배열 사용 -> 방문 여부 체크까지
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n) :
    for j in range(m) :
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True :
            result += 1

print(result) # 정답 출력
