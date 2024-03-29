# P.361 # 정렬 # 성공 # 교재 버전 확인해야
# Q25. 실패율

# 오렐리가 만든 프렌즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자 수가 급감했다.
# 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.
# 이 문제 해결을 위해 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다.
# 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다.
# 오렐리를 위해 실패율을 구하는 코드를 완성하라.
# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열 stages가
# 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨 있는 배열을 return
# 하도록 solution 함수를 완성하라.

# 스테이지 개수 N은 1 이상 500 이하 자연수.
# stages 길이는 1 이상 200,000 이하.
# stages에는 1 이상 N+1 이하의 자연수가 담김. 각 자연수는 현재 도전 중인 스테이지 번호.
# 단, N+1은 마지막 스테이지(N번째 스테이지)까지 클리어한 사용자를 나타냄.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하라.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지 실패율은 0으로 정의.

def solution(N, stages) :
    answer = [] # 결과로 반환할 리스트
    answer1 = [] # 인덱스 = 스테이지로 생각하기
    answer1.append((0,0)) # 0번 스테이지는 없기에 0 삽입해주기
    stage = 1 # 1번부터 N번까지 갈 stage
    player = len(stages) # 전체 플레이어 수
    while stage <= N : # 플레이어가 모든 스테이지 통과한 경우 제외하기 위함
        count = 0
        for i in stages :
            if i == stage :
                count+=1
        # 내림차순 정렬 + 작은 번호의 스테이지가 앞으로 오게 하기 위함
        tmp = (player-count)/player 
        answer1.append((tmp, stage)) # 실패율, 스테이지 저장
        player-=count # 다음 스테이지 도달한 플레이어 수 변경
        stage+=1

    answer1.sort()
    # print(answer1) # 디버깅
    for i in range(1, N+1) :
        answer.append(answer1[i][1])
    return answer

# 임의 입출력을 만들기 위한 코드
# N = int(input())
# stages = list(map(int, input().split()))
# solution(N, stages)

''' 교재 solution '''
# 구현 문제로 분류할 수 있으나 문제 해결 과정에서 정렬 라이브러리가 효과적으로 사용될 수 있어
# 정렬 유형의 문제로 분류.
# 전체 스테이지 개수는 200,000 이하이기 때문에 기본 정렬 라이브러리로 O(NlogN) 시간으로
# 내림차순 정렬을 수행하면 충분함.

# 이 코드는 다음 프로그래머스 사이트에서 테스트해야 정상 동작한다.
# https://programmers.co.kr/learn/courses/30/lessons/42889

'''
def solution(N, stages) :
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N+1) :
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i) # ⭐️ count 함수로 개수 체크 가능

        # 실패율 계산
        if length == 0 :
            fail = 0
        else : 
            fail = count/length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t:t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [[i[0] for i in answer]]
    return answer
'''