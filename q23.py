# P.359 # 정렬 # 성공!
# Q23. 국영수

# 도영이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 다음 조건으로 학생 성적을 
# 정렬하는 프로그램을 작성하라.
# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로(단, 아스키코드에서 대문자는 소문자보다
# 작으므로 사전 순으로 앞에 옵니다.)
# 첫째 줄에 도현이네 반의 학생 수 N(1<=N<=100,000)이 주어진다.
# 둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백 구분해 주어진다.
# 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수다.
# 이름은 알파벳 대소문자로 이루어진 문자열이고 길이는 10자리를 넘지 않는다.
# 문제에 나온 정렬 기준으로 정렬하고 첫째 줄부터 N개의 줄에 걸쳐 각 학생명을 추출한다.

''' 나의 풀이 '''

n = int(input())
arr = []
for _ in range(n) :
    name, kor, eng, mat = input().split()
    kor = int(kor)
    eng = int(eng)
    mat = int(mat)
    arr.append((name, kor, eng, mat))
#print(arr)
arr.sort(key=lambda student : student[0])
sorted1 = sorted(arr, key = lambda student : student[3], reverse=True)
sorted2 = sorted(sorted1, key=lambda student : student[2])
res = sorted(sorted2, key=lambda student : student[1], reverse=True)

for i in res :
    print(i[0])


''' 교재 해결 방법 '''
n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보 입력받기
for _ in range(n) :
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# 우선 순위에 맞게 순서대로 기입해주는 방식

# 정렬된 학생 정보에서 이름만 출력
for student in students :
    print(student[0])