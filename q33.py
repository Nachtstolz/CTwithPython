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

INF = 1e9
n = int(input())
time = [] # 1~n인덱스까지
money = [] # 1~n인덱스까지
res = [0] * (n+1)
max_res = 0
time.append(0)
money.append(0)
for _ in range(n) :
    t, p = map(int, input().split())
    time.append(t)
    money.append(p)

limit = n+1
for i in range(n, 0, -1) :
    #print('i, time[i]+i : ', i, time[i]+i)
    if time[i]+i > limit :
        res[i] = max_res
        continue
    else :
        if time[i]+i == limit :
            res[i] = max(money[i], max_res)
        else :
            res[i] = max(money[i]+res[time[i]+i], max_res)
    max_res = res[i]
    #limit = i
    #print(max_res)


print(max_res)