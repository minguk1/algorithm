T = int(input())
for ts in range(1, T+1):
    count_list = [0] * 1001
    N = int(input())
#
    # bus_stop = []
    for i in range(N):
        num, a, b = map(int, input().split())
        if num == 1:
            for i in range(a, b+1):
                count_list[i] += 1
        elif num == 2:
            for i in range(a, b+1, 2):
                count_list[i] += 1
            # if a % 2 == 0:
            #     for i in range(a, b+1):
            #         if i % 2 == 0:
            #             count_list[i] += 1
            # else:
            #     for i in range(a, b+1):
            #         if i % 2 == 1:
            #             count_list[i] += 1

        elif num == 3:
            if a % 2 == 0:
                for i in range(a, b+1):
                    if i % 4 == 0:
                        count_list[i] += 1
            else:
                for i in range(a, b+1):
                    if (i % 10 != 0) and (i % 3 == 0):
                        count_list[i] += 1

    # print(bus_stop)
    # bus_set = set(bus_stop)
    # result_list = []
    # for i in bus_set:
    #     result_list.append(bus_stop.count(i))
    # print(count_list)
    print(f"#{ts} {max(count_list)}")
