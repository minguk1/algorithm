T = 10
for tc in range(1, T+1):
    num = int(input())
    password = list(map(int, input().split())) + [0,0,0,0,0]

    first = 0
    new = 8
    i = 1
    # print(password)
    while True:
        password[new] = password[first]-i
        if password[new] <= 0:
            password[new] = 0
            result = password[first+1:new+1]
            break
        i += 1
        new += 1
        first += 1
        if i == 6:
            i = 1
            first = 0
            new = 8

            password = password[5:] + [0,0,0,0,0]
            # print(password)
    print(f"#{tc}", end=" ")
    for i in range(len(result)):
        print(result[i], end=" ")
    print()