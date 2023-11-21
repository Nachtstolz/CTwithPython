# P.321 # 구현 # 성공!
# Q07. 럭키 스트레이트

# 게임의 아웃복서 캐릭터는 필살기인 '럭키 스트레이트' 기술이 있습니다.
# 해당 기술은 현재 캐릭터의 점수를 N점이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어
# 왼쪽 부분의 각 자릿수 합과 오른쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황에 사용할 수 있다.
# 예를 들어, 현재 점수 123,402라면 왼쪽 부분의 각 자릿수 합 1 + 2 + 3,
# 오른쪽 부분의 각 자릿수 합 4 + 0 + 2이므로 두 합이 6으로 동일해 기술을 사용할 수 있다.
# 현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 알려주는 프로그램을 작성하라.

# 첫째 줄에 점수 N이 정수로 주어진다(10 <= N <= 99,999,999). 단 점수 N의 자릿수는 항상 짝수다.
# 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"를 출력한다.

n = list(map(int, input()))
mid = len(n)//2

sum1 = 0
sum2 = 0

for i in range(mid) :
    sum1 += n[i]
for j in range(mid, len(n)) :
    sum2 += n[j]

if sum1 == sum2 :
    print("LUCKY")
else :
    print("READY")

## 교재 풀이 방법 :: 왼쪽 자릿수 합 - 오른쪽 자릿수 합 = 0 이용