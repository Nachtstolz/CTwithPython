# P.381 # DP # 성공
# Q35. 못생긴 수

# 못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미한다. 다시 말해 오직 2, 3, 5를 약수로 가지는 합성수이다.
# 1은 못생긴 수라고 가정한다. 따라서 못생긴 수들은 {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15...} 순으로 이어진다.
# 이때 n번째 못생긴 수를 찾는 프로그램을 작성하라. 예를 들어 11번째 못생긴 수는 15이다.

# 첫째 줄에 n이 입력된다 (1<=n<=1,000)

# 12 = 1, 2, 3, 4, 6, 12
n = int(input())
arr = []
arr.append(1)
num = 2
while len(arr) < n :
    # print(num, arr)
    tmp1 = num / 2
    tmp2 = num / 3
    tmp3 = num / 5
    if tmp1 in arr or tmp2 in arr or tmp3 in arr :
        # print(tmp1, tmp2, tmp3, "true")
        arr.append(num)
    num+=1

# print(arr)
print(arr[n-1])
