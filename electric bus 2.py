T= int(input())
for tc in range(1, T+1):

    n, *m = map(int, input().split())
    # print(n, m)

    battery = [0] + m

    # print(battery)

    def move(idx, cnt):
        max_move = idx + battery[idx]

        # 종료 조건
        if len(battery) <= max_move:
            # print("arrive")
            print(f"#{tc} {cnt}")
            return

        max_value = 0
        for i in range(idx+1, max_move+1):
            # print(i)
            if i + battery[i] >= max_value:
                max_value = i + battery[i]
                # print(max_value)
                # print(idx)
                selection = i

        move(selection, cnt+1)

    move(1, 0)
