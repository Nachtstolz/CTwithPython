# P.363 # 정렬 # 성공? -> 실패 # 교재 풀이 참고
# Q26. 카드 정렬하기

# 정렬된 두 묶음의 숫자 카드가 있을 때 각 묶음의 카드 수를 A, B라 하면 보통 두 묶음을 합쳐서
# 하나로 만드는 데에는 A+B번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드
# 묶음을 합치려면 50번의 비교가 필요한다.
# 매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라
# 비교 횟수가 달라진다. 예를 들어, 10장 20장 40장의 묶음이 있다면, 10장과 20장을 합친 뒤 합친 30장과 40장을 합치면
# (10+20) + (30+40) = 100번의 비교가 필요하다.
# 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합치면 (10+40) + (50+20) = 120번의 비교가 필요하다.
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지 구하는 프로그램을 작성하라.

# 첫째 줄에 N이 주어진다. (1<=N<=100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각 크기가 주어진다.
# 첫째 줄에 최소 비교 횟수를 출력한다. (21억 이하)

''' 내 풀이 '''

# 무작정 작은 값들로 첫 sort -> 이후 앞에서부터 더하기하면 된다고 생각
# 반례) 10 20 40 50 60 일 때 문제 발생 정답:390 결과:400

'''
# merge sort -> 검색 참고
def merge_sort(arr) :
    if len(arr) < 2 :
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


n = int(input())
tmp = []
for i in range(n) :
    tmp.append(int(input()))

merge_sort(tmp)
res = tmp[0]+tmp[1]
for i in range(2, len(tmp)) :
    res += res+tmp[i]

print(res)
'''

''' 교재 풀이 '''

# 핵심 아이디어 : 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장
# 매 상황에서 무조건 가장 작은 크기의 두 카드 묶음을 합치면 된다 -> "그리디 알고리즘"으로도 분류 가능
# 다만, 정렬 개념을 활용하는 아이디어가 필요하기 때문에 정렬 유형의 문제로 분류.

# 우선순위 큐 : 항상 가장 작은 크기의 두 카드 묶음을 알고 효과적으로 수행할 수 있는 구조
# 원소를 넣었다 빼는 것만으로도 정렬된 결과를 얻을 수 있음. 힙 자료구조를 이용해 구현할 수 있고
# 파이썬에서는 heapq 라이브러리를 지원. 정렬 및 다익스트라 알고리즘에 대해 다룰 때 heapq 라이브러리 이용한 것과
# 동일하게 사용 가능.

import heapq
n = int(input())

# 힙(heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n) :
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙(heap)에 원소가 1개 남을 때까지
while len(heap) != 1 :
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one+two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
