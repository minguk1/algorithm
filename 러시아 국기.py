T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())

    color = [[0] * 3 for _ in range(n)]
    for i in range(n):
        input_list = list(input())
        for k in input_list:
            if k == "W":
                color[i][0] += 1
            elif k == "B":
                color[i][1] += 1
            else:
                color[i][2] += 1

    # print(color)

    min_change = n * m
    for b_start in range(1, n-1):
        for r_start in range(b_start + 1, n):
            now_sum = 0
            for w in range(0, b_start):
                now_sum += color[w][1] + color[w][2]
            for b in range(b_start, r_start):
                now_sum += color[b][0] + color[b][2]
            for r in range(r_start, n):
                now_sum += color[r][0] + color[r][1]

            if now_sum < min_change:
                # print(b_start, r_start)
                min_change = now_sum

    print(f"#{tc} {min_change}")
