n = 20
memo = [0] * n
memo[1] = 1

def fibo(n):
    # n번째 항을 계산한 적이 없고 n이 2이상이라면
    # n번째 항을 계산해야 된다.
    if n>= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]

print(fibo(7))
print(fibo(19))