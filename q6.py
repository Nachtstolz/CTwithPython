# P.316 # 그리디 # 교재 참고 # 교재 솔루션 추가
# Q06. 무지의 먹방 라이브

# 이 문제는 기본 코드가 제공되므로 링크를 통해 문제를 풀어야 한다.
# https://programmers.co.kr/learn/courses/30/lessons/42891

# 무지는 먹방을 진행하며 다음과 같은 독특한 방식을 생각했습니다.
# 회전판에 먹어야 할 N개의 음식이 있다. 각 음식에는 1~N까지 번호가 붙어있으며, 각 음식을 섭취하는데
# 일정 시간이 소요된다. 무지는 다음과 같은 방법으로 음식을 섭취한다.
# 1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
# 2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
# 3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다. 다음 음식이란 아직 남은 음식 중
#   다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
# 4. 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 가정한다.

# 무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다. 무지는 네트워크 정상화 후 다시 방송을 이어갈
# 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다. 각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 food_times,
# 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return하도록 solution 함수를
# 완성하세요.

# food_times는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열
# k는 방송이 중단된 시간을 나타냄
# 만약 더 섭취해야할 음식이 없다면 -1을 반환

# 정확도 테스트
# food_times의 길이는 1 이상 2000 이하
# food_times의 원소는 1 이상 1000 이하 자연수
# k는 1 이상 2,000,000 이하 자연수

# 효율성 테스트
# food_times의 길이는 1 이상 200,000 이하
# food_times의 원소는 1 이상 100,000,000 이하 자연수
# k는 1 이상 2x10의 13승 이하의 자연수

''' 교재 풀이 '''

' 솔루션 토픽 '
# 모든 음식을 시간 기준으로 정렬, 시간이 적게 걸리는 음식부터 제거해 나가는 방식 이용 : 우선순위 큐를 이용해 구현 가능
# 예를 들어, 3개의 음식이 있고 1번 - 8초 2번 - 6초 3번 - 4초 소요되며 K는 15초이다.

# 첫 단계에서는 가장 적게 걸리는 음식인 3번 음식을 뺀다.
# 단, 음식이 3개 남아있으므로 (남은 음식의 개수) 3 X (3번 음식을 먹는 시간) 4 = 12를 빼야 한다.
# 다시 말해, 3번 음식을 다 먹기 위해서는 12초가 걸린다는 의미이다. 결과적으로 전체 남은 시간은 15초 -> 3초로 줄어든다.

# 전체 남은 시간은 3초이고, 이번 단계에서는 2번 음식을 빼야 한다. 전체 음식이 2개 남아있으므로 이번 단계에서 뺄 시간은
# (남은 음식의 개수) 2 X (2번 음식을 먹는 시간) 6 = 12를 빼야 한다. 하지만, 현재 전체 남은 시간이 3초인데
# 이는 2초보다 작으므로 빼지 않도록 한다. 따라서 '다음으로 먹어야 할' 음식의 번호를 찾아 출력하면 된다.

# 매초 먹어야 할 음식을 일렬로 나열, 전체 남은 시간이 3초이므로 4번째 음식의 번호를 출력하면 정답이다. 따라서 2번 음식.

import heapq

def solution(food_times, k) :
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k :
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)) :
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 저장
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 은식 중 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x : x[1]) # 음식의 번호 기준 정렬
    return result[(k-sum_value) % length][1]


''' 교재 풀이 해설 참고해서 나의 풀이'''

'''
import heapq

def solution(food_times, k) :
    answer = 0

    # 사고가 나기 전 음식을 다 해치웠다면
    # -1인 경우 예외처리 우선) food_times의 총합 <= k 일때 
    all_time = sum(food_times)
    if all_time <= k :
        return -1

    q = []
    # 우선순위 큐에 알아서 음식 먹는 시간 작은 순서대로 정렬되어 삽입
    for i in range(len(food_times)) :
        heapq.heappush(q, (food_times[i], i))

    food_num = len(food_times)
    top = heapq.heappop(q)
    # 오류가 나기 전 시간동안 시간이 가장 적은 한 음식을 다 먹을 수 있는지 판별
    while k >= top[0]*food_num :
        k-=top[0] # 남은 시간
        food_num-=1 # 해치워야할 음식 개수
        food_times[top[1]] = 0
        top = heapq.heappop(q)
    
    start = 0
    end = k
    while True :
        food_times = list(map(lambda x : x-1, food_times))
        if food_times[start:end].count(-1) > 0 :
            end = end+food_times[start:end].count(-1)
            start = end
        else :
            break

    # end의 범위가 리스트의 0인덱스로 다시 오는 경우까지 생각을 못했나...? or 당연히 안오는 건가?
    if end >= food_num :
        answer = end-len(food_times)+1
    print(answer)

    return answer
'''

''' 나의 풀이 - 알고리즘 사용을 눈씻고도 찾아볼 수 없어서 야매로 풀고 있는'''

'''
def solution(food_times, k):
    answer = 0

    # -1인 경우 예외처리 우선) food_times의 총합 <= k 일때
    # food_times의 길이 / k
    # 그때의 몫(a)과 나머지(b)
    # food_times의 각원소에서 a를 뺀 값이 0보다 크거나 같은 지 확인 - > 그 개수(zero) 저장
    # k 포함 이후 인덱스부터 zero의 개수 더하기 (근데 이때 food_times[i]가 0보다 작거나 같다? 넘겨서)
    
    all_time = sum(food_times)
    # -1이 출력되는 경우
    if all_time <= k :
        answer = -1
        return answer

    a = len(food_times) // k
    b = len(food_times) % k

    minus = 0
    food_times = list(map(lambda x : x-a, food_times))
    # 0보다 크거나 같은 값들의 합 저장 -> 어떻게 효율성 있게 할지?
    for i in range(len(food_times)) :
        if food_times[i] <= 0 and i<=b :
            minus+=abs(food_times[i])

    new_b = b+minus
    if new_b >= k :
        food_times = list((map(lambda x : x-1)), food_times[b+1:])
        new_b -= len(food_times)- ...
    


    return answer
'''

solution(list(map(int, input().split())), int(input()))

