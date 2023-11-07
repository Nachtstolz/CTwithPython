# P.182 # 정렬 # 성공!
# 4. 두 배열의 원소 교체

# 동빈이는 두 개의 배열 A, B를 가지고 있다.
# 두 배열은 N개의 원소로 구성, 배열의 원소는 모두 자연수이다.
# 동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 바뀌치기 연산이란
# 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
# 동빈이의 최종 목표는 배열 A의 모든 원소 합이 최대가 되도록 하는 것이다.
# N, K, 그리고 배열 A, B가 주어졌을 때 최대 K번의 바꿔치기 연산을 수행해 만들 수 있는
# 배열 A의 모든 원소 합의 최댓값을 출력하는 프로그램 작성하시오.

# 첫 번째 줄에 N, K 공백으로 구분되어 입력 (1 <= N <= 100,000 / 0 <= K <= N)
# 두 번째 줄에 배열 A의 원소들이 공백 구분 입력. 모든 원소는 10,000,000보다 작은 자연수.
# 세 번째 줄에 배열 B의 원소들이 공백 구분 입력. 모든 원소는 10,000,000보다 작은 자연수.

n, k = map(int, input().split(' '))

arr_a = list(map(int, input().split(' ')))
arr_b = list(map(int, input().split(' ')))
# print(arr_a, arr_b)

arr_a = sorted(arr_a)
arr_b = sorted(arr_b, reverse=True)

for i in range(k) :
    if arr_a[i] < arr_b[i] :
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else : 
        break

#print(arr_a)
print(sum(arr_a))