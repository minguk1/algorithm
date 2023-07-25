T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    pizza_list = list(map(int, input().split()))

    next_i = 0

    oven = [0] * 1000
    ofront = orear = -1

    for i in range(n):
        orear += 1
        oven[orear] = [i, pizza_list[i]]
        next_i += 1
    remain = n

    last_index = -1

    while True:
        ofront += 1
        i, pizza = oven[ofront]

        pizza //= 2

        if pizza != 0:
            orear += 1
            oven[orear] = [i, pizza]

        else:
            if next_i < m:
                orear += 1
                oven[orear] = [next_i, pizza_list[next_i]]

                next_i += 1

            else:
                remain -= 1
                if remain == 0:
                    last_index = i
                    break
    print(f"#{tc} {last_index+1}")