n = 1000000
is_prime = [True for i in range(n+1)]
for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        j = 2
        while i*j <= n:
            is_prime[i*j] = False
            j += 1


T = int(input())
for ts in range(1, T+1):
    count = 0
    # result = []
    D, A, B = map(int, input().split())
    for k in range(A, B+1):
        if is_prime[k] == True and str(D) in str(k):
            if k == 1 and A == 1:
                pass
            else:
                count += 1
            # result.append(k)

    # print(result)
    print(f"#{ts} {count}")
    # print(result)