def change(a):
    if a == "0001101":
        return 0
    elif a == "0011001":
        return 1
    elif a == "0010011":
        return 2
    elif a == "0111101":
        return 3
    elif a == "0100011":
        return 4
    elif a == "0110001":
        return 5
    elif a == "0101111":
        return 6
    elif a == "0111011":
        return 7
    elif a == "0110111":
        return 8
    elif a == "0001011":
        return 9
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    password = [""]*n
    for i in range(n):
        password[i] = input()

    # print(password)

    for i in range(n):
        for j in range(m-1, -1, -1):
            if password[i][j] == "1":
                s, t = i, j
                break
        if password[i][j] == "1":
            s, t = i, j
            break
    # print(s, t)
    # print(password[s][t-6:t+1])
    result = [0]*8
    cnt = 0
    while cnt < 8:
        word = password[s][t-6:t+1]
        result[7-cnt] = change(word)
        cnt += 1
        t = t - 7
    # print(result)
    first_sum = 0
    second_sum = 0
    for i in range(4):
        first_sum += result[2*i]
        second_sum += result[2*i+1]
    # print(first_sum, second_sum)
    if (3*first_sum + second_sum) % 10 == 0:
        final = first_sum + second_sum
    else:
        final = 0

    print(f"#{tc} {final}")