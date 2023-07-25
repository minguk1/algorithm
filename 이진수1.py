T = int(input())
for tc in range(1, T+1):

    a, b = input().split()
    n = int(a)
    change_list = [""]*n
    result = [""]*n

    for i in range(n):
        k = int(b[i], 16)
        cnt = 0
        while True:

            change_list[i] += str(k % 2)
            k = k // 2
            cnt += 1
            if cnt == 4:
                break
    # print(change_list)
    for i in range(n):
        for j in range(4):
            result[i] += change_list[i][3-j]
    # print(result)
    print(f"#{tc}", end=" ")
    for i in range(n):
        print(result[i], end="")
    print()