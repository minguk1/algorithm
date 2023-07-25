n = 1000
is_prime = [True for i in range(n+1)]
for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        j = 2
        while i*j <= n:
            is_prime[i*j] = False
            j += 1

T = int(input())
for ts in range(1, T+1):
    N = int(input())

    # print(is_prime)
    sosu_list = []
    for j in range(2, N-1):
        if is_prime[j] == True:
            sosu_list.append(j)

    # print(sosu_list)
    cnt = 0


    for i in sosu_list:
        for j in sosu_list:


            if (N - i - j) in sosu_list:
                if i <= j <= (N-i-j):
                    cnt += 1
                    # print(i,j,N-i-j)
                        # print(i,j,k)
                        #     cnt += 1
                        #     print(i,j,k)
                        # elif i==j or j ==k or k == i:
                        #     cnt += 1/3
                        #     print(i,j,k)
                        # else:
                        #     cnt += 1/6
                        #     print(i,j,k)

    # print(cnt)
    result = cnt
    print(f"#{ts} {result}")