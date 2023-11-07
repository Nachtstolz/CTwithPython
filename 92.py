# P.92 # 그리디 # 성공!
# 2. 큰 수의 법칙

# 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가
# 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상
# 10000 이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

n, m, k = map(int, input().split(' '))
# print(n, m, k) # 입력 값 테스트
li = list(map(int, input().split(' ')))
# print(li) # 입력 값 테스트

li.sort()
i = li[len(li)-1]
j = li[len(li)-2]

print(i, j)
res = 0
p = 0
while p < m :
    for q in range(k) :
        res += i
        p += 1
        if p >= m :
            break
    if p >= m :
        break
    res += j
    p += 1
    
print(res)

# 예쁜 코드 및 해답 코드 1 : 반복문 정리
# while True :
#     for i in range(k) : # 가장 큰 수를 k번 더하기
#         if m == 0 : # m이 0이라면 반복문 탈출
#             break
#         res += p
#         m -= 1 # 더할 때마다 1씩 빼기
#     if m == 0 : # m이 0이라면 반복문 탈출
#         break
#     res += q # 두 번째로 큰 수를 한 번 더하기
#     m -= 1 # 더할 때마다 1씩 빼기

# print(res)

# 예쁜 코드 및 해답 코드 2 : 시간 초과 문제 해결, 반복되는 수열 파악

# cnt = m / (k+1) * k # 가장 큰 수가 등장하는 횟수
# cnt += m % (k+1) # 나머지가 있을 때 가장 큰 수가 더해지는 횟수 추가

# res = 0
# res += (cnt) * p # 가장 큰 수 더해주기
# res += (m-cnt) * q # 총 더하는 수 - 가장 큰 수 등장 횟수 = 두 번쨰 큰 수 등장 횟수
# print(res)