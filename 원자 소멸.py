


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))
        # a, b, c, d = map(int, input().split())
        # if c == 0:
        #     A[i] = [a, b+t, d]
        # elif c == 1:
        #     A[i] = [a, b-t, d]
        # elif c == 2:
        #     A[i] = [a-t, b, d]
        # else:
        #     A[i] = [a+t, b, d]
    # print(A)
    B = [[0]*4 for i in range(N)]
    for i in range(N):
        if A[i][2] == 0:
            B[i] = [A[i][0], A[i][1] , A[i][3]]

        elif A[i][2] == 1:

            B[i] = [A[i][0], A[i][1] , A[i][3]]

        elif A[i][2] == 2:

            B[i] = [A[i][0] , A[i][1], A[i][3]]

        else:
            B[i] = [A[i][0] , A[i][1], A[i][3]]

    t = 0
    energy = 0
    life = N
    while t <= 2000:
        t = t + 0.5
        # print(t)
        for i in range(N):
            if A[i][2] == 0:
                if B[i][2] != 0:
                    B[i] = [A[i][0], A[i][1] + t, A[i][3]]
                else:
                    "1"
                    B[i][0] = -5000*(i+1)
                    life -= 1
            elif A[i][2] == 1:
                if B[i][2] != 0:
                    B[i] = [A[i][0], A[i][1] - t, A[i][3]]
                else:
                    "2"
                    B[i][0] = -5000*(i+1)
                    life -= 1
            elif A[i][2] == 2:
                if B[i][2] != 0:
                    B[i] = [A[i][0] - t, A[i][1], A[i][3]]
                else:
                    "3"
                    B[i][0] = -5000*(i+1)
                    life -= 1
            else:

                # print("here")
                if B[i][2] != 0:
                    B[i] = [A[i][0] + t, A[i][1], A[i][3]]
                else:
                    "4"
                    B[i][0] = -5000*(i+1)
                    life -= 1
                # print(" ds")
                # print(A)
        if life <= 1:

            break
        # print(B)
        for i in range(N):
            for j in range(i+1, N):

                if B[i][0] == B[j][0]:
                    if B[i][1] == B[j][1]:
                        # print(B[i], B[j])
                        energy += B[i][2]
                        energy += B[j][2]
                        B[i][2] = 0
                        B[j][2] = 0
                        # print(t, energy)
                        # print(B[i], B[j])
                        # print(B[i][2], B[i][2])
    print(f"#{tc} {energy}")