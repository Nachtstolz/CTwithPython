# P.378 # DP # 풀이 완료 # 교재 참고 풀이 하단 기재
# Q32. 정수 삼각형

#     7
#    3 8
#   8 1 0
#  2 7 4 4
# 4 5 2 6 5
# 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.
# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 / 오른쪽에 있는 것 중 선택 가능.
# 삼각형의 크기는 1 이상 500 이하이다. 삼각형의 값 범위는 0 이상 9999 이하. 각 수는 모두 정수.

# 첫째 줄에 삼각형의 크기 n(1<=n<=500)이 주어지고, 둘째 줄부터 n+1째 줄까지
# 정수 삼각형이 주어진다.
# 합이 최대가 되는 경로에 있는 수의 합을 출력.

''' 내 풀이 '''
'''
n = int(input())
dp = []
arr = []
for _ in range(n) :
    arr.extend(list(map(int, input().split())))
dp.append(arr[0])
dp.append(arr[0]+arr[1])
dp.append(arr[0]+arr[2])
idx=1
for i in range(2, n) : # i = 4
    idx+=i # idx = 10
    for j in range(0, i) :
        n_idx = idx+j
        if j == 0 :
            dp.append(dp[n_idx-i]+arr[idx])
        else :
            dp.append(max(dp[n_idx-i], dp[n_idx-(i+1)]) + arr[n_idx])
    dp.append(dp[idx-1]+arr[idx+i])

print(max(dp))
'''

''' 교재 풀이 '''
# 특정 위치로 도달하기 위해서는 1. 왼쪽 위 혹은 2. 바로 위 2가지 위치에서만 내려올 수 있다.
# 따라서 모든 위치를 기준으로 이전 위치로 가능한 2가지 위치까지의 최적합 중 더 큰 합을 가지는 경우 선택한다.
# 기본적인 점화식은 다음과 같다.
# dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
# 단, dp 테이블에 접근해야 할 때마다 리스트의 범위를 벗어나지 않는지 체크할 필요가 있다.
# 또한 구현 편의상 초기 데이터를 담는 array 변수를 사용하지 않고 바로 dp 테이블에
# 초기 데이터를 담아서 점화식에 따라 dp 테이블을 갱신할 수 있다.

n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 dp 테이블 초기화 

for _ in range(n) :
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
for i in range(1, n) :
    for j in range(i+1) :
        # 왼쪽 위에서 내려오는 경우
        if j == 0 :
            up_left = 0
        else : 
            up_left = dp[i-1][j-1]
        # 바로 위에서 내려오는 경우
        if j == 0 :
            up = 0
        else :
            up = dp[i-1][j]

        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))