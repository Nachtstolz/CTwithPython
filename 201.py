# P.201
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
def binary_search(list, res, start, end) :
    if end < start :
        return 0
    
    mid = (start+end) // 2
    total = 0

    for i in list :
        if i - list[mid] > 0 :
            total += (i-list[mid])
    
    print(total, res)
    if total >= m and list[mid] > res :
        res = list[mid]
    elif list[mid] > res : # 19 vs 15
        return binary_search(list, res, start, mid-1)
    else : # total > m에만 해당 # 10 vs 15
        return binary_search(list, res, mid+1, end)
    
binary_search(li, res, 0, n-1)
print(res)
        
    
