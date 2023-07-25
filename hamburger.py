T = int(input())
for tc in range(1, T+1):

    n, limit = map(int, input().split())

    taste_list = [0] * n
    cal_list = [0] * n
    for i in range(n):
        taste_list[i], cal_list[i] = map(int, input().split())

    max_taste = 0
    def select(i, cal, taste):
        global max_taste, limit

        if cal > limit:
            return
        if taste + sum(taste_list[i:n]) < max_taste:
            return

        # 종료 조건
        if i == n:
            if cal <= limit:
                if taste >= max_taste:
                    max_taste = taste
            return


        select(i+1, cal + cal_list[i], taste + taste_list[i])
        select(i+1, cal, taste)

    select(0, 0, 0)
    print(f"#{tc} {max_taste}")
