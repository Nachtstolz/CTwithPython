# P.226 # DP # 교재 참고
# 5. 효율적인 화폐 구성
# N가지 종류의 화폐가 있다. 이 화폐의 개수를 최소한 이용해서 그 가치의 합이 M원이 되도록 한다.
# 이 때 각 화폐는 몇 개라도 사용할 수 있고, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 간주.
# 예를 들어, 2, 3원 단위의 화폐가 있을 때 15원을 만들기 위해 3원을 5개 쓰는 것이 최소한의 화폐 개수.

# 첫쩨 줄에 N, M이 주어진다.(1<=N<=100, 1<=M<=10,000)
# 이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수.
# 첫째 줄에 경우의 수 X를 출력하고 불가능할 때는 -1을 출력.

''' 교재 참고 '''
# 금액 i로 만들 수 있는 최소한의 화폐 개수를 ai, 화폐의 단위를 k라고 했을 때
# 점화식은 a(i-k)를 만드는 방법이 존재할 경우, ai = min(ai, a(i-k)+1) 이다.
# 존재하지 않는 경우는 ai = 10,001.
# 이 때, a(i-k)는 금액 (i-k)를 만들 수 있는 최소한의 화폐 계수를 의미한다.
# 이 점화식을 모든 화폐 단위에 대해 적용하면 됨. K 크기의 리스트를 할당, 각 인덱스를 '금액'으로 고려해 메모리제이션.

# 단계 정리
# 1. 초기화 : 각 인덱스에 해당 값으로 10001을 설정. (M의 최대 크기가 벗어나도록 설정.)
#    인덱스 0의 값은 0으로 설정.
# 2. (2, 3, 5 화폐 단위 가정 하) 첫 번째 화폐 단위인 2 확인. 인덱스 2인 경우 1값을 가지는데
#    즉, a2 = a0+1이다. 인덱스 4의 경우 2값을 가지는데 a4 = a2+1이다.
# 3. 두 번째 화폐 단위인 3 확인. a5 = a2+1로 2라는 값을 가지고, 이는 2원짜리 화폐 1개, 3원짜리 화폐 1개로 구성.
# 4. 세 번째 화폐 단위인 5 확인. a7 = a2+1로 2라는 값을 가진다.
#    원래 이전 단계에서 a7값은 2+2+3로 3이었는데 현 단계에서 2+5로 2값으로 갱신된다.

n, m = map(int, input().split())
li = []
for i in range(n) :
    li.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [10001] * (m+1)

# DP 진행 (보텀업)
dp[0] = 0
for i in range(n) :
    for j in range(li[i], m+1) :
        if dp[j-li[i]] != 10001 : # (i-k)원을 만드는 법이 존재할 때
            # if 문은 사실 없어도 됨. 10001값을 가지더라도 어차피 항상 dp[j] 즉, 10001값 반환해서.
            dp[j] = min(dp[j], dp[j-li[i]]+1)
            # 이미 7값이 2 + 2 + 3 으로 dp[7]에 저장된 상황에서
            # 2 + 5로 dp[7] 값을 갱신하기 위함

# 계산된 결과 출력
if dp[m] == 10001 :
    print(-1)
else :
    print(dp[m])