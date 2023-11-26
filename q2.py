# P.312 # 그리디 # 성공
# Q02. 곱하기 혹은 더하기
# 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인해
# 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라.
# 단, +보다 x를 먼저 계산하는 일방적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.
# 예를 들어 02984라는 문자열이 주어지면, 만들어질 수 있는 가장 큰 수는 ((((0+2)x9)x8)x4)=576이다.
# 또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어진다.
# 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다.(1<=S의 길이<=20)

s = list(map(int, input()))

res = s[0]
for i in range(1, len(s)) :
    if res + s[i] > res * s[i] :
        res+=s[i]
    else :
        res*=s[i]
print(res)

''' 교재 코드 필사 '''
# 두 수 중 하나라도 0 혹은 1일 경우 더하기 수행이 효율적. 
# 두 수에 대해 연산할 때 두 수 중에 하나라도 1 이하인 경우엔 더하며, 두 수가 모두 2 이상인 경우 곱하기
data = input()

# 첫 번째 문자를 숫자로 변경해 대입
result = int(data[0])
for i in range(1, len(data)) :
    # 두 수 중 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num
print(result)