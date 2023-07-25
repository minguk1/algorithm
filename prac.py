T = int(input())

for p in range(1, T+1):


    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    e = [ ]
    # print(a[0], b[0])
    if N<=M:
        for k in range(0, M-N+1):
            d = [ ]
            for i in range(0, N):
                c = a[i] * b[i+k]

                d.append(c)

            # print((d))
            # print(sum(d))
            e.append(sum(d))
        # print(e)
        print(f"#{p} {max(e)}")

    if N>M:
        for k in range(0, N-M+1):
            d = [ ]
            for i in range(0, M):
                c = a[i+k] * b[i]

                d.append(c)

            # print((d))
            # print(sum(d))
            e.append(sum(d))
        # print(e)
        print(f"#{p} {max(e)}")
