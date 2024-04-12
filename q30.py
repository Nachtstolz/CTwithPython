# P.370 # 이진 탐색 # 성공? # 교재 풀이 필사 예정
# Q30. 가사 탐색

# https://programmers.co.kr/learn/courses/30/lessons/60060
# 이 문제는 기본 코드가 제공되므로 상기 링크를 통해서 문제를 풀어야 함

# 친구들로부터 천재 프로그래머로 불리는 '프로도'는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에
# 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해달라는 제안을 받았습니다.
# 그 제안 사항 중, 키워드는 와일드카드 문자 중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다.
# 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다.
# 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.
# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때, 각 키워드별로
# 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해주세요.

# words의 길이(가사 단어의 개수)는 2 이상 100,000 이하
# 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없음.
# 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하.
# 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공
# 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함되지 않는 것으로 가정.

# queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하
# 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없음.
# 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하.
# 검색 키워드는 중복 가능. 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?'로만 구성되어 있으며 특수문자, 숫자 포함 X
# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함되어 있으며 '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로 주어짐.
    # - 예를 들어 "??odo", "fro??", "?????"는 가능한 키워드
    # - 반면에 "frodo"(?가 없음), "fr?do"(?가 중간에 있음), "?ro??"(?가 양쪽에 있음)는 불가능 키워드

def solution2(words, queries) :
    answer = []

    for search in queries :
        tmp = list(search)
        length = len(tmp)
        idx = 0
        first = 0
        last = 0
        # 앞에 ?가 올 경우
        if tmp[0] == '?' :
            for i in range(0, len(tmp)) :
                if tmp[i] != '?' :
                    idx = i
                    tmp = tmp[idx:]
                    first = length - len(tmp)
                    break
        else : # 뒤에 ?가 올 경우
            for i in range(0, len(tmp)) :
                if tmp[i] == '?' :
                    idx = i-1
                    tmp = tmp[:idx+1]
                    last = length - len(tmp)
                    break

        # print(tmp)
        # print(first, last)
        res = 0
        for each in words :
            each = list(each)
            if len(each) != len(tmp)+first+last : # 길이 다르면 컷
                continue

            num = 0
            # print(tmp, each)
            if last == 0 : # 앞에 ?가 올 때
                for i in range(len(tmp)) :
                    if tmp[i] == each[i+idx] :
                        num += 1
            else : # 뒤에 ?가 올 때
                for i in range(len(tmp)) :
                    if tmp[i] == each[i] :
                        num+=1

            if num == len(tmp) :
                res+=1

        answer.append(res)

    # print(answer)
    return answer

# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# solution(words, queries)

''' 교재 풀이 '''

# 각 단어를 길이에 따라 나눈다. 이후 모든 리스트 정렬 -> 각 쿼리에 대해 이진 탐색 수행
# 예를 들어, 문제의 예시와 같이 전체 단어가 ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# 로 구성되어 있을 때 길이에 따라 나눈 후 정렬하면 아래와 같다.
# 길이가 5인 단어 리스트 : ["frame", "frodo", "front", "frost", "kakao"]
# 길이가 6인 단어 리스트 : ["frozen"]
# 이제 "fro??"라는 쿼리가 들어왔다고 가정하면, "fro??"는 길이가 5이므로 길이가 5인 단어 리스트에서 "fro"로 시작하는 
# 모든 단어를 찾으면 된다. 이때 구체적으로 이진 탐색을 이용해 "fro"로 시작되는 마지막 단어의 위치를 찾고, "fro"로 시작하는
# 첫 단어의 위치를 찾아 그 위치의 차이를 계산하면 될 것이다. 이처럼 이진 탐색으로 특정 단어가 등장한 횟수를 게산할 수 있다.

# 혹은 "fro??"라는 쿼리가 들어왔을 때, 부록에서 다루었던 count_by_range() 함수를 이용하여 "froaa"보다 크거나 같으면서
# "frozz"보다 작거나 같은 단어의 개수를 세도록 구현하면 매우 간단하다.

# 다만, 문제에서는 와일드카드 "?"가 접두사에서도 등장할 수 있다고 하였다. 만약 "????o"라는 쿼리가 들어왔다고 가정하자.
# 이는 기존의 리스트인 ["frame", "frodo", "front", "frost", "kakao"]를 이용해서 처리할 수가 없을 것이다.
# 따라서 접두사에 와일드카드가 등장하는 것을 처리하기 위해 기존 단어를 뒤집은 단어를 담고 있는 리스트 또한 별도 선언해야 한다.
# 현재 예시에서는 길이가 5인 뒤집힌 단어 리스트는 ["emarf", "oakak", "odorf", "tnorf", "tsorf"]이다.
# 결과적으로 접두사에 와일드카드가 등장하는 경우, 뒤집힌 단어 리스트를 대상으로 이진 탐색을 수행하면 된다.

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
# 앞서 설명한대로 right_value - left_value 인덱스로 계산도 가능
def count_by_range(a, left_value, right_value) :
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries) :
    answer = []
    for word in words : # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

    for i in range(10001) : # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries : # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?' : # 접미사에 와일드카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else : # 접두사에 와일드카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수 저장
        answer.append(res)
    return answer

# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# print(solution(words, queries))