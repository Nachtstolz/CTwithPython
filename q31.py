# P.375 # DP # 교재 참고
# Q31. 금광

# n x m 크기의 금광이 있습니다. 금광은 1x1 크기의 칸으로 나누어져 있고, 각 칸은 특정 크기의 금이 들어있다.
# 채굴자는 첫 번째 열부터 출발해 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
# 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라.
# 첫째 줄에 테스트 케이스 T가 입력된다 (1<=T<=1000).
# 매 테스트 케이스 첫째 줄에 n과 m이 공백 구분되어 입력된다. (1<=n,m<=20) 둘째 줄에 n x m개의 위치에
# 매장된 금의 개수가 공백으로 구분되어 입력된다. (1<=매장된 금의 개수<=100)
# 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력한다. 각 테스트 케이스는 줄 바꿈을 이용해 구분한다.

t = int(input())
for _ in range(t) : # 테스트 케이스 수 만큼 반복
    n, m = map(int, input().split()) # n,m 크기 입력
    li = [] 
    tmp = list(map(int, input().split())) # 테스트 케이스 입력

    idx = 0
    for i in range(n) : # 테스트 케이스 2차원 배열로 입력
        li.append(tmp[idx:idx+m])
        idx+=m

    for j in range(1, m) :
        for i in range(n) :
            # 왼쪽 위
            if i == 0 :
                left_up = 0
            else :
                left_up = li[i-1][j-1]
            # 왼쪽 아래
            if i == n-1 :
                left_down = 0
            else :
                left_down = li[i+1][j-1]
            # 왼쪽
            left = li[i][j-1]
            li[i][j] = li[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n) :
        result = max(result, li[i][m-1])
    print(result)