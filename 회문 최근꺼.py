T = 10
for ts in range(1, T+1):


    a = input()

    A = [0]*100
    for i in range(100):
        A[i] = list(input())

    B = [[0]*100 for i in range(100)]

    for i in range(100):
        for j in range(100):
            B[i][j] = A[100-1-j][i]

    cnt = 0
    #A
    l = 0 #홀수
    m = 0 #짝수
    #B
    n = 0 #홀스
    o = 0 #짝수
    #홀수
    for i in range(100):
        for j in range(0, 100):
            t = 0
            while (j-t>=0) and (j+t)<100:

                if A[i][j-t] == A[i][j+t]:
                    t += 1
                    if (j-t ==0) or (j+t) == 99:
                        if A[i][j - t] == A[i][j + t]:
                            if t > l:
                                l = t

                else:
                    t -= 1
                    if t > l:
                        l = t

                    break
    for i in range(100):
        for j in range(0, 100):
            t = 0
            while (j-t >= 0) and (j+t)<100:

                if B[i][j-t] == B[i][j+t]:
                    t += 1
                    if (j-t == 0) or (j+t) == 99:
                        if B[i][j - t] == B[i][j + t]:
                            if t > n:
                                n = t

                else:
                    t -= 1
                    if t > n:
                        n = t

                    break




    #짝수
    for i in range(100):
        for j in range(0, 99):
            t = 1
            while (j-t+1>=0) and (j+t < 100):

                if A[i][j-t+1] == A[i][j+t]:
                    t += 1
                    if j - t + 1 == 0 or j + t == 99:
                        if A[i][j - t + 1] == A[i][j + t]:
                            if t > m:
                                m = t
                            break

                else:
                    t -= 1
                    if t > m:

                        m = t


                    break


    for i in range(100):
        for j in range(0, 99):
            t = 1
            while (j-t+1>=0) and (j+t < 100):

                if B[i][j-t+1] == B[i][j+t]:
                    t += 1
                    if j - t + 1 == 0 or j + t == 99:
                        if B[i][j - t + 1] == B[i][j + t]:
                            if t > o:
                                o = t
                            break

                else:
                    t -= 1
                    if t > o:

                        o = t

                    break

    result = max(2*l+1, 2*m, 2*n+1, 2*o)
    print(f"#{ts} {result}")