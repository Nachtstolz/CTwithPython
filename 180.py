# P.180 # 정렬 # 성공!
# 3. 성적이 낮은 순서로 학생 출력하기

# N명의 학생 정보가 있다. 학생 정보는 학생 이름과 성적으로 구분된다.
# 성적이 낮은 순서대로 학생 이름을 출력하는 프로그램을 작성하시오.

# 첫 번째 줄에 학생의 수 N이 입력된다. (1<=N<=100,000)
# 두 번째 줄부터 N+1번째 줄에는 학생 이름을 나타내는 문자열 A와 학생 성적을 나타내는 정수 B가
# 공백으로 구분되어 입력된다. 문자열 A의 길이와 학생의 성적은 100 이하 자연수이다.
# 모든 학생 이름을 성적이 낮은 순서로 출력한다. 성적이 동일한 학생 순서는 자유롭게 출력한다.

n = int(input())
arr = []

def setting(data) :
    return data[1]

for _ in range(n) : 
    name, score = input().split(' ')
    tmp = (name, int(score))
    arr.append(tmp)

arr.sort(key=setting)

for i in arr :
    print(i[0], end=' ')


''' lambda 사용하는 방법 '''
# array = sorted(array, key=lambda student: student[1])

# for student in arr :
#   print(student[0], end=' ')