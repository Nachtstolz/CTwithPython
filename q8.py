# P.322 # 정렬 # 성공!
# Q08. 문자열 재정렬
# 알파벳 대문자의 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로
# 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다.
# 첫째 줄에 하나의 문자열 S가 주어진다. (1<=S의 길이<=10,000)

s = list(input()) # 첫 입력 문자열
sum = 0 # 숫자 총 합 구할 변수
length = len(s) # 문자열의 길이
idx = 0 # 문자열을 돌아다닐 인덱스

while idx < length : 
    if ord(s[idx]) < 65 : # 65보다 크거나 같으면 문자
        sum+=int(s.pop(idx)) # 숫자인 경우 리스트에서 빼내 총합에 더하기
        idx-=1 # 인덱스가 더해지지 않게 한 번 빼기
        length -= 1 # 숫자 값이 리스트에서 빠졌기에 길이 반영
    idx+=1 # 다음 인덱스로 넘어가기
s.sort() # 문자열 리스트 정렬하기
for i in s :
    print(i, end='')
if sum > 0 :
    print(sum)
    

''' 교재 코드 '''
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data :
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha() :
        result.append(x)
    # 숫자는 따로 더하기
    else :
        value+=int(x)

# 알파벳을 오름차순으로 정리
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0 :
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환해 출력)
print(''.join(result))