T = int(input())

for tc in range(1, T+1):

    total = list(map(int, input().split()))

    a = [total[0], total[2]]
    b = [total[1], total[3]]
    win = 0
    for i in range(4,12):
        x = total[i]
        # a 차례
        if i % 2 == 0:
            a.append(x)
            # triple 로 이기는 경우
            if a.count(x) == 3:
                win = 1
                # print("1 tri")
                break
            # run 으로 이기는 경우
            if (x-1 in a and x-2 in a) or (x-1 in a and x+1 in a) or(x+1 in a and x+2 in a):
                win = 1
                # print("1 run")
                break
        # b 차례
        else:
            b.append(x)
            # triple 로 이기는 경우
            if b.count(x) == 3:
                win = 2
                # print("2 tri")
                break
            # run 으로 이기는 경우
            if (x - 1 in b and x - 2 in b) or (x - 1 in b and x + 1 in b) or (x + 1 in b and x + 2 in b):
                win = 2
                # print("2 run")
                break

    print(f"#{tc} {win}")