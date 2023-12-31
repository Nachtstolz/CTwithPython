# P.378 # DP
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

n = int(input())
dp = []
arr = []
for _ in range(n) :
    arr.extend(list(map(int, input().split())))
print(arr)
dp.append(arr[0])
dp.append(arr[0]+arr[1])
dp.append(arr[0]+arr[2])
idx=1
for i in range(2, n) : # i = 4
    idx+=i # idx = 10
    for j in range(0, i) :
        n_idx = idx+j
        if j == 0 :
            dp.append(dp[n_idx]+arr[idx])
        else :
            dp.append(max(dp[n_idx-i], dp[n_idx-(i+1)]) + arr[n_idx])
    dp.append(dp[idx-1]+arr[idx+i])
    print(dp)

print(max(dp))