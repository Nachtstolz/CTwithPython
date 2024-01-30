# P.377 # DP # 교재도움
# Q33. 퇴사

# 상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다. 오늘부터 N+1번째 되는 날 퇴사를 하기 위해, 남은 N일 도안
# 최대한 많은 상담을 하려고 한다. 비서에게 최대한 많은 상담을 잡을 것을 부탁했고 하루 하나씩 서로 다른 상담을 잡았다.
# 각 상담은 상담 완료에 걸리는 시간 Ti와 상담으로 받는 금액 Pi로 이루어진다.
# 상담에 필요 기간은 1일보다 클 수 있기에 모든 상담을 할 수는 없다.
# 또한 N+1일 째에는 회사에 없기 때문에 상담할 수 없는 일자가 있다.
# 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하라.

# 첫째 줄에 N(1<=N<=15)이 주어진다.
# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다.
# (1<=Ti<=5, 1<=Pi<=1,000)
# 첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력하라.


n = int(input())
time = [] # 1~n인덱스까지
money = [] # 1~n인덱스까지
res = [0] * (n+1) # 최대 이익 계산할 배열
max_res = 0 # 최종 결과를 저장할 (최대 이익 저장)
time.append(0) # 0 인덱스를 날리기 위해
money.append(0) # 0 인덱스를 날리기 위해

for _ in range(n) : # t와 p (시간별 비용) 입력 받기
    t, p = map(int, input().split())
    time.append(t)
    money.append(p)

limit = n+1 # 최대 상담 기간
# ⭐️ 교재 참고 설명 # 마지막날부터 체크하기 # 탑다운 방식
for i in range(n, 0, -1) : # n부터 1까지
    if time[i]+i > limit : # 현재 날 + 기간이 최대 상담 기간 넘어갈 때(즉, 근무 기간을 넘을 때)
        res[i] = max_res
        continue
    else :
        if time[i]+i == limit : # res에 저장된 값이 없을 경우
            res[i] = max(money[i], max_res)
        else :
            res[i] = max(money[i]+res[time[i]+i], max_res)
    max_res = res[i]


print(max_res)

''' 교재 해결 방안 '''
# 1일 차에 상담을 진행하는 경우, 최대 이익은 '1일 차의 상담 금액 + 4일부터의 최대 상담 금액'이 된다.
# 이 원리를 이용해 뒤쪽 날짜부터 거꾸로 계산하여 문제를 해결할 수 있다.
# 즉, 뒤쪽부터 매 상담에 대해 '현재 상담 일자의 이윤(p[i]) + 현재 상담 마친 일자부터의 최대 이윤(dp[t[i]+i])'
# 를 계산하면 된다. 이후 계산된 각각의 값 중에 최댓값을 출력하면 된다.
# 'dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익'이라고 하면 점화식은
# dp[i] = max(p[i]+dp[t[i]+i], max_value)가 된다. 이때 max_value는 뒤에서부터 계산할 때,
# 현재까지의 최대 상담 금액에 해당하는 변수이다.

'''
n = int(input())
t = [] # 각 상담을 완료하는 데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

for _ in range(n) :
    x,y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1) :
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n :
        # 점화식에 맞게, 현재까지의 최고 이익 게산
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else :
        dp[i] = max_value

print(max_value)
'''