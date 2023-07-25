T = 10
for ts in range(1, T+1):

    M = int(input())
    A = [0]*8
    for i in range(8):
        A[i] = list(input())

    B = [[0]*8 for i in range(8)]

    for i in range(8):
        for j in range(8):
            B[i][j] = A[8-1-j][i]

    # print(A)
    # print(B)
    result = 0
    t = M//2
    if M % 2 == 1:
        for j in range(8):
            for i in range(t, 8 - t):
                num_count = 0
                for k in range(1, t + 1):
                    if A[j][i - k] == A[j][i + k]:

                        num_count += 1

                if num_count == t:
                    result += 1

    else:
        for j in range(8):
            for i in range(t-1, 8-t):
                num_count = 0
                for k in range(1, t+1):
                    if A[j][i+1-k] == A[j][i+k]:
                        num_count += 1


                if num_count == t:
                    result += 1

    if M % 2 == 1:
        for j in range(8):
            for i in range(t, 8 - t):
                num_count = 0
                for k in range(1, t + 1):
                    if B[j][i - k] == B[j][i + k]:
                        num_count += 1

                if num_count == t:
                    result += 1

    else:
        for j in range(8):
            for i in range(t - 1, 8 - t):
                num_count = 0
                for k in range(1, t + 1):
                    if B[j][i + 1 - k] == B[j][i + k]:
                        num_count += 1

                if num_count == t:
                    result += 1
    print(f"#{ts} {result}")