T = int(input())
for ts in range(1, T+1):
    N = int(input())
    A = [[0]*N for _ in range(N)]

    A[0][0] = 1
    i = 0
    j = 0
    change_count = N - 1
    k = 0
    p = 1
    while True:
        if p + 1 == N ** 2 + 1:
            break
        else:

            while True:
                if p + 1 == N**2 + 1:
                    break
                if k == change_count:
                    k = 0
                    break
                else:
                    k += 1
                    p += 1
                    j += 1
                    if A[i][j] > 0:
                        k = 0
                        p -= 1
                        j -= 1
                        break
                    A[i][j] = p

            while True:
                if p + 1 == N**2 + 1:
                    break
                if k == change_count:
                    k = 0
                    break
                else:
                    k += 1
                    p += 1
                    i += 1
                    if A[i][j] > 0:
                        k = 0
                        p -= 1
                        i -= 1
                        break
                    A[i][j] = p

            while True:
                if p + 1 == N**2 + 1:
                    break
                if k == change_count:
                    k = 0
                    change_count -= 1
                    break
                else:
                    k += 1
                    p += 1
                    j -= 1
                    if A[i][j] > 0:
                        k = 0
                        p -= 1
                        j += 1
                        break
                    A[i][j] = p

            while True:
                if p + 1 == N**2 + 1:
                    break
                if k == change_count:
                    k = 0
                    break
                else:
                    k = 0
                    p += 1
                    i -= 1
                    if A[i][j] > 0:
                        k -= 1
                        p -= 1
                        i += 1
                        break
                    A[i][j] = p
    print(f"#{ts}")
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=" ")
        print()