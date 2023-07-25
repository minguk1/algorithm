T = int(input())
for ts in range(1, T+1):

    N, M = map(int, input().split())
    A = [0]*N
    t = M//2
    # print(A)
    for i in range(N):
        A[i] = list(input())

    # print(A[10])

    if M%2 == 1:
        for j in range(N):
            for i in range(t, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if A[j][i-k] == A[j][i+k]:
                        # print(j,i,k)
                        num_count += 1
                        p = i
                if num_count == t:
                    print(f"#{ts} {''.join(A[j][p-t:p+t+1])}")

    else:
        for j in range(N):
            for i in range(t-1, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if A[j][i+1-k] == A[j][i+k]:
                        num_count += 1
                        p = i
                        # print(j, i, k)
                if num_count == t:
                    print(f"#{ts} {''.join(A[j][p-t+1:p+t+1])}")

    B = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            B[i][j] = A[N-1-j][i]
    # print(B)
    if M%2 == 1:
        for j in range(N):
            for i in range(t, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if B[j][i-k] == B[j][i+k]:
                        # print(j,i,k)
                        num_count += 1
                        p = i
                if num_count == t:
                    print(f"#{ts} {''.join(B[j][p-t:p+t+1])}")

    else:
        for j in range(N):
            for i in range(t-1, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if B[j][i+1-k] == B[j][i+k]:
                        num_count += 1
                        p = i
                        # print(i, k)
                if num_count == t:
                    print(f"#{ts} {''.join(B[j][p-t+1:p+t+1])}")

    C = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            C[i][j] = B[N - 1 - j][i]

    if M%2 == 1:
        for j in range(N):
            for i in range(t, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if C[j][i-k] == C[j][i+k]:
                        # print(j,i,k)
                        p = i
                        num_count += 1
                if num_count == t:
                    print(f"#{ts}c {''.join(C[j][p-t:p+t+1])}")

    else:
        for j in range(N):
            for i in range(t-1, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if C[j][i+1-k] == C[j][i+k]:
                        num_count += 1
                        p = i
                        # print(i, k)
                if num_count == t:
                    print(f"#{ts}c {''.join(C[j][p-t+1:p+t+1])}")

    D = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            D[i][j] = C[N - 1 - j][i]
    print(D)

    if M%2 == 1:
        for j in range(N):
            for i in range(t, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if D[j][i-k] == D[j][i+k]:
                        # print(j,i,k)
                        num_count += 1
                        p = i
                if num_count == t:
                    print(f"#{ts}d {''.join(D[j][p-t:p+t+1])}")

    else:
        for j in range(N):
            for i in range(t-1, N-t):
                num_count = 0
                for k in range(1, t+1):
                    if D[j][i+1-k] == D[j][i+k]:
                        num_count += 1
                        p = i
                        # print(i, k)
                if num_count == t:
                    print(f"#{ts}d {''.join(D[j][p-t+1:p+t+1])}")
