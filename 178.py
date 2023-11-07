# P.178 # 정렬 # 성공!
# 2. 위에서 아래로

# 수가 크기 상관없이 나열되어 있다. 큰 수 부터 작은 수 순서로 정렬하는 프로그램을 만드시오.
# 첫째 줄에 수열에 속한 수의 개수 N이 주어진다.
# 둘째 줄부터 N+1 번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하 자연수.

n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(input()))
arr.sort(reverse=True)

for i in arr :
    print(i, end = ' ')