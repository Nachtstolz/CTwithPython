# P.368 # 이진 탐색
# Q28. 고정점 찾기

# 고정점 : 수열의 원소 중 그 값이 인덱스와 동일한 원소
# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있고 오름차순 정렬되어 있다.
# 이때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하라.
# 고정점이 없다면 -1을 출력하라.
# 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받는다.

# 첫째 줄에 N이 입력된다. (1<=N<=1,000,000)
# 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다. 

''' 교재 해법 중 노트 '''
# 시간 복잡도 O(logN)으로 고정점을 찾기 위해서는 선형 탐색으로는 해결 불가능.
# 때문에 이진 탐색을 수행해 빠르게 고정점을 찾아야 한다.
# 이미 배열이 정렬되어 있기에 이진 탐색 사용 가능.

def binary_search(arr, start, end) :
    if start > end :
        print(-1)
        return

    mid = (start+end)//2
    if mid == arr[mid] : # 서치 완료 시
        print(mid)
        return
    elif arr[mid] > mid :
        binary_search(arr, start, mid-1)
    else :
        binary_search(arr, mid+1, end)
    

n = int(input())
arr = list(map(int, input().split()))
# arr.sort() # 이미 배열이 정렬되어 있다고 명시됨.
binary_search(arr, 0, n-1)


''' 교재에서 표현한 binary_search code '''
'''
def binary_search(arr, start, end) :
    if start > end :
        return None # None 반환 시 -1 출력되게 외부에서 조건문.

    mid = (start+end)//2
    if mid == arr[mid] : # 서치 완료 시
        return mid
    elif arr[mid] > mid :
        return binary_search(arr, start, mid-1)
    else :
        return binary_search(arr, mid+1, end)
'''