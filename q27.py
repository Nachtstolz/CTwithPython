# P.367 # 이진 탐색 # 교재 참고
# Q27. 정렬된 배열에서 특정 수의 개수 구하기

# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x=2라면, 4를 출력한다.
# 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받는다.
# 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력된다. (1<=N<=1,000,000)
# 수열의 원소 중 값이 x인 원소의 개수를 출력. 단, 값이 x인 원소가 하나도 없다면 -1을 출력.

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메소드
def count_by_value(array, x) :
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않을 경우
    if a == None :
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메소드
def first(array, target, start, end) :
    if start > end :
        return None
    
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중 가장 왼쪽에 있는 경우만 인덱스 반환
    if array[mid] == target and (mid == 0 or target > array[mid-1]) :
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우
    elif target <= array[mid] :
        return first(array, target, 0, mid-1)
    else :
        return first(array, target, mid+1, end)
    
# 마지막 위치를 찾는 이진 탐색 메소드
def last(array, target, start, end) :
    if start > end :
        return None
    
    mid = (start+end) // 2
    # 해당 값을 가지는 원소 중 가장 오른쪽에 있는 경우만 인덱스 반환
    if array[mid] == target and (mid == n-1 or target < array[mid+1]) :
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif target < array[mid] :
        return last(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else :
        return last(array, target, mid+1, end)
    
n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 x인 데이터 개수 계산
cnt = count_by_value(array, x)

# 값이 x인 원소가 존재하지 않으면
if cnt == 0 :
    print(-1)
else :
    print(cnt)

'''파이썬 내 이진 탐색 라이브러리 bisect를 활용했을 경우'''
from bisect import bisect_left, bisect_right

# bisect_left(a,x) : 정렬된 a에 x를 삽입할 위치를 리턴. x가 a에 이미 있으면 기존항목의 앞(왼쪽) 위치 반환.
# bisect_right(a,x) : bisect_left와 거의 유사. x가 a에 이미 있으면 기존 항목 뒤(오른쪽) 위치 반환.

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value) :
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n,x = map(int, input().split())
array = list(map(int, input()))

# 값이 [x, x] 범위에 있는 데이터 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0 :
    print(-1)
else :
    print(count)
