T = int(input())
for tc in range(1, T+1):

    n = int(input())
    start_list = []
    end_list = []
    i_list = [0] * 201
    for i in range(n):
        start, end = map(int, input().split())
        print(start, end)
        if start % 2 == 1:
            a = start//2 + 1
            start_list.append(a)
        else:
            a = start // 2
            start_list.append(a)
        if end % 2 == 1:
            b = end // 2 + 1
            end_list.append(b)
        else:
            b = end // 2
            end_list.append(b)
        if a < b:
            print(a, b)
            for k in range(a, b+1):

                i_list[k] += 1
        elif b < a:
            print(a, b)
            for k in range(b, a+1):
                i_list[k] += 1
    # i = 0
    # cnt = 0
    # max_cnt = 0
    # # print(start_list)
    # # print(end_list)
    # while i <= 200:
    #     i += 1
    #     if i in start_list:
    #         cnt += start_list.count(i)
    #         if cnt > max_cnt:
    #             max_cnt = cnt
    #         continue
    #     if i in end_list:
    #         cnt -= end_list.count(i)
    #     if i == 200:
    #         break
    # print(f"#{tc} {max_cnt}")
    print(f"{tc} {max(i_list)}")