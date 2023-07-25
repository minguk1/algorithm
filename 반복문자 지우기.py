T = int(input())
for tc in range(1, T+1):

    s = input()
    s_list=list(s)
    i = 0
    n = len(s)
    while True:
        if s_list[i] == s_list[i+1]:
            b = s_list.pop(i+1)
            c = s_list.pop(i)
            n -= 2
            # print(n)
            # print(s_list)
            i = 0
        else:
            i += 1
        if i == n-1:
            break

    result = len(s_list)
    print(f"#{tc} {result}")