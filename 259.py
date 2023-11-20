# P.259 # 최단 거리 # 교재 참고 -> 교재 사용 방식 : 플로이드 워셜 
# 2. 미래 도시
# 방문 판매원 A는 많은 회사가 모여 있는 공중 미래 도시에 있다.
# 공중 미래 도시에는 1~N번까지의 회사가 있는데, 특정 회사끼리는 도로로 연결되어 있다.
# 방문 판매원 A는 현재 1번 회사에 있고, X번 회사에 방문해 물건을 판매하고자 한다.
# 특정 회사에 도착하기 위해선 연결 도로를 이용하는 방법이 유일하다. 연결된 회사는 양방향 이동이 가능하다.
# 도로는 마하의 속도로 사람을 이동시켜 도로가 연결되어 있다면 정확히 1만큼의 시간으로 이동할 수 있다.
# 또한, 방문 판매원 A는 K번 회사의 상대방과 소개팅에 참석해야 한다.
# 결국, A는 X번 회사에 물건을 판매하기 전, 먼저 소개팅 상대의 회사에 찾아가 함께 커피를 마셔야 하기에 
# 1번 회사에서 출발 -> K번 회사에 방문 -> X번 회사로 가는 것이 목표이고 가능한 빠르게 이동하려고 한다.
# 방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

# 첫째 줄에 전체 회사 개수 N과 경로 회수 M이 공백 구분되어 주어진다. (1<=N, M<=100)
# 둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
# M+2번째 줄에는 X와 K가 공백 구분되어 차례로 주어진다.(1<=K<=100)
# X번 회사에 도달할 수 없다면 -1을 출력한다.

''' 리스트 사용해서 풀이하기 '''
n, m = map(int, input().split())
arr = []
# ⭐️ 배열 생성법 유의 또 유의! 
res = [[9999] * (n+1) for _ in range(n+1)]

for _ in range(m) : 
    tmp = tuple(map(int, input().split()))
    arr.append(tmp)
    res[tmp[0]][tmp[1]] = 1
    res[tmp[1]][tmp[0]] = 1

arr.sort() #key = lambda item : item[0]
x, k = map(int, input().split())

# 전체 비용 산정
for a in range(1, n+1) :
    for b in range(1, n+1) :
        for r in range(1, n+1) :
            res[a][b] = min(res[a][b], res[a][r]+res[r][b])

out = res[1][k] + res[k][x]
if out > 9999 :
    print(-1)
else :
    print(out)
    
''' 만약 다익스트라 알고리즘으로 구현한다면 ? '''
# visited 배열을 통해 방문 여부 체크하고
# 방문하지 않은 노드 + 가장 짧은 거리에 있는 노드 선택
# 거리는 정해져있지 않기 때문에 for 문을 사용해 1씩 증가한 시간 저장.
# 1 -> k, k -> x 의 경우를 따로 진행하기.