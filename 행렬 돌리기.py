#
T = int(input())

for t in range(1, T+1):


    n = int(input())
    J = []

    for m in range(0, n):
        J.append(list(map(int, input().split())))

    print(J)


    K = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            K[i][j] = J[n-1-j][i]

    print(K)
    # L = [[0]*n for i in range(n)]
    #
    # for i in range(n):
    #     for j in range(n):
    #         L[i][j] = K[n-1-j][i]
    #
    #
    # M = [[0]*n for i in range(n)]
    #
    # for i in range(n):
    #     for j in range(n):
    #         M[i][j] = L[n-1-j][i]
    # print(f"#{t}")
    # for i in range(n):
    #     for j in range(n):
    #         print(K[i][j], end="")
    #     print(" ", end="")
    #     for j in range(n):
    #         print(L[i][j], end="")
    #     print(" ", end="")
    #     for j in range(n):
    #         print(M[i][j], end="")
    #     print("")