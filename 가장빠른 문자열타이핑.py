T = int(input())
for ts in range(1, T+1):

    a, b = input().split()

    cnt = 0
    while True:
        if b in a:
            a = a.replace(b, "", 1)
            cnt += 1
            # print(a)
        else:
            cnt += len(a)
            break


    print(f"#{ts} {cnt}")