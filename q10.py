# P.325 # 구현 # 교재 풀이 필사 # 추후 다시 풀어보기
# Q10. 자물쇠와 열쇠

# 고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득한 것으로 추정되는 비밀의 문을 발견했다.
# 문을 열려고보니 자물쇠로 잠겨있었고, 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 설명해주는
# 종이가 있었다. 자물쇠는 격자 한 칸의 크기가 1x1인 NxN 크기의 정사각 격자 형태이고 특이한 모형의
# 열쇠는 MxM 크기인 정사각 격자 형태로 되어 있다. 자물쇠에는 홈이 파여있고 열쇠 또한 홈과 돌기 부분이 있다.
# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열린다.
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향 X 그러나 자물쇠 영역 내 열쇠의 돌기
# 부분과 자물쇠의 홈 부분이 정확히 일치해야하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다.
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.

# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
# 열쇠로 자물쇠를 열 수 있으면 true, 열 수 없으면 false를 return하도록 solution 함수를 완성하라.

# key는 MxM(3<=M<=20, M은 자연수) 크기 2차원 배열이다.
# lock은 NxN(3<=N<=20, M은 자연수) 크기 2차원 배열이다.
# M은 항상 N 이하이다.
# key와 lock의 원소는 0 또는 1로 이루어져 있고, 0은 홈 1은 돌기 부분을 나타낸다.

# 기본 코드 링크 : https://programmers.co.kr/learn/courses/30/lessons/60059 

# 두 배열의 값을 합했을 때 0 or 2인 원소가 있다면 회전 / 이동 생각
# 회전했을 때 lock의 홈 방향과 key의 돌기 모양이 같은 부분이 있음을 알아채면 되는
 
''' 교재 풀이법 '''
# 완전 탐색
# 완전 탐색을 수월하게 하기 위해 자물쇠 리스트 크기를 3배 이상으로 변경.
# 예를 들어 열쇠와 자물쇠가 3x3 크기일 때 가장 먼저 자물쇠를 크기가 3배인 새로운 리스트로 만들어
# 중앙으로 옮긴다. 이후 열쇠 배열을 왼쪽 위부터 시작해서 한 칸씩 이동하는 방식으로 차례대로 자물쇠의 모든 홈을
# 채울 수 있는지 확인한다.

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a) :
    n = len(a) # 행의 길이 계산
    m = len(a[0]) # 열의 길이 계산
    result = [[0] * n for _ in range(m)]
    for i in range(n) :
        for j in range(m) :
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠 중간 부분이 모두 1인지 확인 (자물쇠 크기를 3배로 늘린 후 중앙에 위치시켰기 때문)
def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
            if new_lock[i][j] != 1 :
                return False
    return True

def solution(key, lock) :
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
    for i in range(n) :
        for j in range(n) :
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4가지 방향에 대해 확인
    for rotation in range(4) :
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n*2) :
            for y in range(n*2) :
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True :
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]
    return False

#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
