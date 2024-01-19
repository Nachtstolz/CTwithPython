# P. 323 # 구현 # 성공!
# Q09. 문자열 압축

# 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부하는데, 문자열에서 같은 값이
# 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현해 더 짧은 문자열로 줄여서 표현하는
# 알고리즘을 공부하고 있다.
# 간단한 예로, "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한 번만 나타난 경우 1 생략)
# 와 같이 표현할 수 있는데, 이러한 방식은 반복 문자가 적은 경우 압축률이 낮다는 단점이 있다.
# 이를 해결하기 위해 문자열을 1개 이상의 단위로 잘라 압축하는 방법을 제시하는데,
# "ababcdcdababcdcd"의 경우 문자를 2개 단위로 자르면 "2ab2cd2ab2cd"로, 8개 단위로 자르면
# "2ababcdcd"로 표현할 수 있다. 이 경우가 가장 짧게 압축해 표현할 수 있는 방법이다.
# 또 다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라 압축하면 "abcabc2de"가 되지만
# 3개 단위로 자르면 "2abcdede"가 되어 가장 짧은 압축법이 된다.
# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축할 경우,
# 가장 짧은 것의 길이를 return하도록 solution 함수를 완성하라.

# s의 길이는 1 이상 1,000 이하이고, 알파벳 소문자로만 이루어져 있다.

#import time

def solution(s) :
    answer = 0
    arr = list(s) # 받은 문자열 리스트에 저장
    # 최대 길이 : len(arr) // 2
    min_len = len(arr) # 문자열 압축 실패 시 최대 길이로 초기화 = i:1
    for i in range(1, len(arr)//2+1) : 
        #time.sleep(3)
        tmp = arr[0:i] # i개 단위로 자른 문자열 중 첫 번째
        start = i # 비교할 문자열의 시작 지점
        res = 0 # 압축 문자열의 길이를 저장할 변수
        count = 1
        # double = False # 두 번 이상 같은지 체크하는 변수
        while start < len(arr) :
            #print(tmp, arr[start:start+i]) # 디버깅
            if tmp == arr[start:start+i] : # 다음 문자열과 같을 경우
                # (⭐️ 책과 비교 후 수정) 해당 경우 앞에 추가할 숫자가 10이상이 되면 반영 못함
                # if double == False :
                # res+=(1) # 앞에 추가할 2, 3같은 숫자 개수만 추가
                count+=1 
                #double = True
            else :
                if count >= 2 : # 중복된 문자열의 개수가 2이상일 경우
                    res+=len(str(count))
                res+=i # tmp 문자열의 길이 더해주기
                count=1
                # double = False
            tmp = arr[start:start+i] # 비교할 tmp 갱신
            start+=i # start 값 변경
        if count >= 2 :
            res+=len(str(count))
        res+=len(tmp) # 마지막에 비교당한 문자열의 길이 더해주기
        #print(min_len, res) # 디버깅
        min_len = min(min_len, res)

    answer = min_len
    return answer

# print(solution(input())) # 임의 테스트를 위해 만든 입출력 함수

''' 책 내 답안 '''
# 이 코드는 다음 프로그래머스 사이트에서 테스트해야 정상 작동한다.
# https://programmers.co.kr/learn/courses/30/lessons/60057

'''
def solution(s) :
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1) :
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step) :
            # 이전 상태와 동일하다면 압축 횟수 (count) 증가
            if prev == s[j:j+step] :
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else :
                compressed += str(count) + prev if count >= 2 else prev
                # 압축할 문자열이 있었다면 count 값과 문자열 넣기, 아닐 경우는 문자열만
                prev = s[j:j+step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해 처리
        compressed += str(count)+prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
'''