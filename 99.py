# P.99
# 4. 1이 될 때까지

# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는
# 최소 횟수를 구하는 프로그램을 작성하시오.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다. (N이 K로 나누어떨어질 때만 선택 가능)

n, k = map(int, input().split(' '))
res = 0
while n!=1 :
    while(n % k != 0) :
        n-=1
        res+=1
    n/=k
    res+=1

print(res)
