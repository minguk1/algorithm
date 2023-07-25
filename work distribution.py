T = int(input())
for tc in range(1, T+1):

    n = int(input())

    work = [0] * n
    for i in range(n):
        work[i] = list(map(int, input().split()))
    j_list = [0] * n
    max_per = 0

    def distri(i, per):
        global max_per

        if i == n:
            if per > max_per:
                max_per = per

            return
        if per < max_per:
            return

        if per == 0:
            return

        for j in range(n):
            if j_list[j] == 0:
                if work[i][j] == 0:
                    continue
                j_list[j] = 1
                per = per * work[i][j] / 100
                distri(i+1, per)
                per = per / work[i][j] * 100
                j_list[j] = 0


    distri(0, 1)
    print(f"#{tc} {round(max_per*100, 6):.6f}")