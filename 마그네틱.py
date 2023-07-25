T = 10
for tc in range(1, T+1):

    n = int(input())

    arr = [0] * 100
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    table = list(map(list, zip(*arr)))
    # print(table)
    total = 0
    for i in range(100):
        k = table[i].index(1)
        # print(i, k)
        stack = 0
        cnt = 0
        while True:

            k += 1
            if k == 100:
                if stack == 1:
                    cnt += stack
                break
            if table[i][k] == 0:
                continue
            elif table[i][k] == 1:
                cnt += stack
                stack = 0
            elif table[i][k] == 2:
                stack = 1



        total += cnt

    print(f"#{tc} {total}")