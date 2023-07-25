T = int(input())
for tc in range(1, T+1):
    n = int(input())

    numbers = set()
    i = 0
    while True:
        i += 1
        t = n * i
        t_list = list(str(t))
        for s in t_list:
            numbers.add(s)

        if len(numbers) == 10:

            break
    print(f"#{tc} {t}")