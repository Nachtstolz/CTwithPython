# P.201 # 이진탐색 # 성공
# 3. 떡볶이 떡 만들기

# 동빈이는 여행 가신 부모님을 대신해 떡집 일을 하기로 했다. 떡볶이 떡을 만들기로 했는데,
# 떡볶이 떡의 길이가 일정하지 않다. 대신 한 봉지 내의 떡 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
# 높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15로 설정하면
# 자른 뒤 높이는 15, 14, 10, 15cm가 되고 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm로
# 손님은 6cm 길이를 가져간다. 손님이 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해
# 설정할 수 있는 절단기의 높이 최댓값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.(1 <= N <= 1,000,000 / 1 <= M <= 2,000,000,000)
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이 총합은 항상 M 이상으로 손님은 필요한 양만큼 떡을 사갈 수 있다.

n, m = map(int, input().split(' '))
li = list(map(int, input().split(' ')))

li.sort()
# print(li)
res = 0

# 재귀 풀이 - 직접
def binary_search(list, res, start, end) :
    if end < start :
        return res
    
    mid = (start+end) // 2
    total = 0

    for i in list :
        if i - mid > 0 :
            total += (i-mid)
    
    if total >= m and mid > res :
        res = mid
        return binary_search(list, res, mid+1, end)
    elif total < m : # 19 vs 15
        return binary_search(list, res, start, mid-1)
    #else : # total > m에만 해당 # 10 vs 15
        
    
res = binary_search(li, res, 0, li[n-1])
print(res)
        

# 반복문 풀이 - 교재 참고
# 현재 얻을 수 있는 떡볶이 양에 따라 자를 위치를 정해야 하기에,
# 재귀로 구현하는 것이 귀찮은 작업이 될 수도 있음.
# 때문에 일반적으로 파라메트릭 서치 문제 유형은 이진 탐색을 반복문을 이용해 구현하는 편.

'''
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end) :
    total = 0
    mid = (start + end) // 2
    for x in array :
        # 잘랐을 때의 떡 양 개산
        if x > mid :
            total += x - mid   
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m :
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else :
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
        start = mid+1

# 정답 출력
print(result)
'''