# P.369 # 이진 탐색 # 교재 참고
# Q29. 공유기 설치

# 도현이의 집 N개가 수직선 위에 있다. 각각의 집 좌표는 x1, x2, ... xn이고, 집 여러개가
# 같은 좌표를 가지는 일은 없다. 언제 어디서나 와이파이를 즐기기 위해 집에 공유기 C개를 설치하려고 한다.
# 최대한 많은 곳에서 와이파이를 사용하려고 하기에 한 집에는 공유기를 하나만 설치할 수 있고,
# 가장 인접한 두 공유기 사이 거리를 가능한 크게 해 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이 거리를 최대로 하는 프로그램 작성하라.

# 첫째 줄에 집의 개수 N(2<=N<=200,000)과 공유기의 개수 C(2<=C<=N)가 하나 이상의 빈칸을 사이에 두고 주어진다.
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 Xi(1<=Xi<=1,000,000,000)가 한 줄에 하나씩 주어진다.

# 모든 조합을 만들어서 확인해볼 수 없기 때문에
n, c = map(int, input().split()) # 입력 받기
house = [] # 집 위치 저장 배열
for _ in range(n) :
    house.append(int(input()))
house.sort() # 오름차순 정렬 

''' 교재 설명 참고 코드 짜기 '''
max_gap = house[n-1] - house[0] # 최대 gap(두 공유기 사이 거리)
min_gap = house[1] - house[0] # 최소 gap
res = 0

while min_gap <= max_gap : # 이진 탐색
    mid = (max_gap + min_gap) // 2
    res = mid
    std = house[0] # 맨 앞 값을 기준으로 gap만큼 더해줬을 때 C란 개수가 나오는지 확인
    count = 1 # 설치 가능한 공유기 수. 첫번째 위치엔 일단 설치.
    for i in range(1, n) : # 맨 앞에부터 차근차근
        if house[i] - std >= mid :
            count+=1
            std = house[i]
    if count < c : # 설치 가능한 공유기 수가 C보다 작으면 gap을 줄여야
        max_gap = mid-1
    else : # 설치 가능한 공유기 수가 C보다 크거나 같으면 gap 늘리기
        min_gap = mid+1

print(res)

''' 교재 솔루션 코드 '''
# 이진 탐색으로 '가장 인접한 두 공유기 사이 거리'를 조절해가며, 매 순간 실제로 공유기를 설치하여
# C보다 많은 개수로 공유기를 설치할 수 있는지 체크해 문제를 해결할 수 있다.
# 다만, '가장 인접한 두 공유기 사이 거리'의 최댓값을 찾아야 하므로, C보다 많은 개수로 공유기를 설치할 수 있다면
# '가장 인접한 두 공유기 사이 거리'의 값을 증가시켜 더 큰 값에 대해서도 성립하는지 체크하기 위해 재탐색한다.
# 이진 탐색을 이용해 해결할 수 있는 ⭐️파라메트릭 서치 유형⭐️의 문제로 이해 가능하다.

'''
# 집의 개수(N)와 공유기의 개수(C)를 입력받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n) :
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬

start = array[1] - array[0] # 집의 좌표 중 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중 가장 큰 값
result = 0

while(start <= end):
    mid = (start+end) // 2 # mid는 가장 인접한 두 공유기 사이 거리(gap) 의미
    value = array[0]
    count = 1
    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n) : # 앞에서부터 차근차근 설치
        if array[i] >= value+mid :
            value = array[i]
            count+=1

    if count>=c : # C개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
        start = mid+1
        result = mid # 최적의 결과 저장
    else : # C개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        end = mid-1

print(result)
'''