# P.197 # 성공!
# 2. 부품 찾기

# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유 번호가 있다.
# 어느 날 손님이 M개 종류의 부품 대량 구매를 원한다며 견적서롤 요청했다.
# 동빈이는 손님이 문의한 부품 M개 종류를 모두 확인해 견적서를 작성해야 한다.
# 가게 안에 부품이 모두 있는지 확인하는 프로그램 작성해라.
# 손님이 요청한 부품 번호의 순서대로 부품이 있으면 yes, 없으면 no를 공백 구분해 출력한다.

# 첫째 줄에 정수 N이 주어진다(1 <= N <= 1,000,000)
# 둘째 줄에 공백 구분해 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
# 셋째 줄에는 정수 M이 주어진다(1 <= M <= 100,000)
# 넷째 줄에는 공백 구분한 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.

import sys

def binary_search(arr, target, start, end) :
    mid = (start+end)//2
    if target == arr[mid] : # 일치하는 문자 찾았을 때
        print("yes", end=' ')
        return 0
    
    if start > end : # 일치하는 문자 못찾았을 때
        print("no", end=' ')
        return 0
    elif target < arr[mid] :
        binary_search(arr, target, start, mid-1)
    elif target > arr[mid] :
        binary_search(arr, target, mid+1, end)

n = int(input())
n_arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
m = int(input())
m_arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

n_arr.sort()

for i in m_arr :
    binary_search(n_arr, i, 0, n-1)

''''''''''''''''''''''''''''''''
''' 계수 정렬을 사용한 방법(교재 참고) '''
''''''''''''''''''''''''''''''''

n = int(input())
arr = [0] * 1000001

# 가게에 있는 전체 부품 번호 입력받아 기록
for i in input().split() :
    arr[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백 구분해 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호 하나씩 확인
for i in x :
    if arr[i] == 1 :
        print('yes', end=' ')
    else :
        print('no', end=' ')

''''''''''''''''''''''''''''''''
''' 집합 자료형 이용 방법(교재 참고) '''
''''''''''''''''''''''''''''''''

# N(가게의 부품 개수)을 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
arr = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분해 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x : # in 을 사용해서 집합 내부에 해당 요소 있는지 확인
    # 해당 부품이 존재하는지 확인
    if i in arr :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')



