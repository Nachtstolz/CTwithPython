# P.346 # DFS/BFS # 성공
# Q18. 괄호 변환

# https://programmers.co.kr/learn/courses/30/lessons/60058
# 이 문제는 기본 코드가 제공되므로 상기 링크를 통해서 문제를 풀어야 합니다

# 카카오에 신입 개발자로 입사한 '콘'은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한
# 소스코드를 분석하여 문제점을 발견, 수정하라는 업무 과제를 받았다. 소스를 컴파일해 로그를 보니 대부분 소스코드 내
# 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 됐다.
# 수정해야 할 소스 파일이 너무 많아서 고민하던 '콘'은 소스코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로
# 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 한다.

# 용어의 정의
# '('와 ')'로만 이루어진 문자열이 있을 경우, '('의 개수와 ')'의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부른다.
# 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부른다.
# 예를 들어, "(()))("와 같은 문자열은 "균형잡힌 괄호 문자열"이지만 올바른 괄호 문자열은 아니다.
# 반면에 "(())()"와 같은 문자열은 "균형잡힌 괄호 문자열"이면서 동시에 올바른 괄호 문자열이다.
# '('와 ')'로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열"이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있다
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환한다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리한다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
#    v는 빈 문자열이 될 수 있다.
# 3. 수행한 결과 문자열을 u에 이어 붙인 후 반환한다.
#   3-1. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행한다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정으르 수행한다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙인다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
#   4-3. ')'를 다시 붙인다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
#   4-5. 생성된 문자열을 반환한다.
# "균형잡힌 괄호 문자열" p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return하도록 해라.

# p는 '('와 ')'로만 이루어진 문자열이며 길이는 2 이상 1,000 이하인 짝수이다.
# 문자열 p를 이루는 '('와 ')'의 개수는 항상 같다.
# 만약 p가 이미 올바른 괄호 문자열이라면 그대로 return하면 된다.

def solution(p):
    if len(p) == 0 : # 빈 문자열을 받았을 때
        return p
    else :
        res = []
        total = 0 # 올바른 & 균형있는 괄호 문자열 확인을 위한 변수
        right = True # 올바른 괄호 문자열 확인
        start = 0
        tmp_start = 0
        tmp_end = 0
        for i in range(start, len(p)) :
            if len(p) == 0 :
                break
            if p[i] == '(' :
                total+=1
            else :
                total-=1
            if total < 0 :
                right = False
            
            if total == 0  : # u를 출력하기
                # u가 올바른 괄호 문자열인지 확인하기
                if right == True : # 올바를 때
                    res.append(p[start:i+1]) # u는 저장
                    start = i+1
                    continue # v에 대해 이어서 수행
                else : # 올바르지 않을 때
                    if tmp_end == 0 :
                        res.append('(')
                        tmp_start = start
                        tmp_end = i
                        start = i+1
                        continue
                    res.append(p[start:i+1])
                    start = i+1
        if right == False :
            res.append(')')
            for i in range(tmp_start+1, tmp_end) :
                if p[i] == '(' :
                    res.append(')')
                else :
                    res.append('(')
    res = ''.join(res)
    print(res)

    return res

solution(input())


''' 교재 풀이 '''
# 구현이나 마찬가지이지만 DFS의 핵심인 재귀함수 구현을 요구하기 때문에 DFS/BFS로 분류

'''
# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p) :
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1
        if count == 0 :
            return i
        
# "올바른 괄호 문자열"인지 판단
def check_proper(p) :
    count = 0 # 왼쪽 괄호의 개수
    for i in p :
        if i == '(' :
            count += 1
        else :
            if count == 0 : # 쌍이 맞지 않는 경우 False 반환
                # 괄호 세트 시작이 )일 때 여기에서 걸림
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p) :
    answer = ''
    if p == '' : # 비어있는 문자열을 받았을 때 / v가 비어있을 때
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    # "올바른 괄호 문자열"이라면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u) :
        answer = u + solution(v) # v에 대해 재귀
    # "올바른 괄호 문자열"이 아니라면 아래의 과정 수행
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list([u[1:-1]]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)) :
            if u[i] == '(' :
                u[i] = ')'
            else :
                u[i] = '('
        answer += "".join(u)
    return answer
'''
