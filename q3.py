# P.313 # 그리디 알고리즘 # 성공!
# Q03. 문자열 뒤집기

# 다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를
# 같게 만들려고 한다. 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
# 예를 들어 S = 0001100일 때는 다음과 같다.
# 전체를 뒤집으면 1110011 -> 4~5번째 문자를 뒤집으면 1111111이 되어 두 번만에 모두 같은 숫자가 된다.
# 하지만 처음부터 4~5번째 문자까지 뒤집으면 한 번에 0000000이 되어 1번 만에 모두 같은 숫자로 만들 수 있다.
# 문자열 S가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하라.

# 첫째 줄에 0과 1로만 이루어진 문자열 S가 주어지고, 문자열의 길이는 100만보다 작다.
# 첫째 줄에 다솜이가 해야 하는 행동의 최소 횟수를 출력한다.

# 1100100 -> 0000100 -> 0000000
# 역전은 큰 영향을 미치지 못하지 않을까 -> just 소수의 숫자를 주로
arr = list(map(int, input()))
n = arr.count(0)
m = arr.count(1)
res = 0
if n > m : # 1 -> 0으로
    for i in range(len(arr)) :
        if arr[i] == 1 :
            if i == 0 or arr[i-1] != arr[i] :
                res += 1            
else : # 0 -> 1로
    for i in range(len(arr)) :
        if arr[i] == 0 :
            if i == 0 or arr[i-1] != arr[i] :
                res += 1
print(res)

''' 교재 풀이 '''
# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중 더 적은 횟수를 가지는 경우 계산
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫번째 원소에 대해서 처리
if data[0] == '1' :
    count0 += 1
else :
    count1 += 1

# 두 번째 원소부터 모든 원소 확인
for i in range(len(data)-1) :
    if data[i] != data[i+1] :
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1' :
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else :
            count1 += 1

print(min(count0, count1))