T = int(input())
for ts in range(1, T+1):
    bus_list = []
    N = int(input())

    # for i in range(N):
    #     a, b = map(int, input().split())
    #     for j in range(a, b+1):
    #         count_list.append(j)
    # print(count_list)
    # STOP = int(input())
    # stop_list = []
    # for i in range(STOP):
    #     p = int(input())
    #     stop_list.append(p)
    # print(stop_list)
    # print(f"#{ts}", end=" ")
    # for p in stop_list:
    #     print(count_list.count(p), end=" ")
    # print("\n")

    for i in range(N):
        a, b = map(int, input().split())
        bus_list.append((a, b+1))
    # print(bus_list)

    STOP = int(input())
    stop_list = []
    for i in range(STOP):
        p = int(input())
        stop_list.append(p)
    # print(stop_list)
    print(f"#{ts}", end=" ")
    for p in stop_list:
        p_count = 0
        for i in range(N):
            if p in range(bus_list[i][0], bus_list[i][1]):
                p_count += 1
        print(p_count, end=" ")
    print("", end="\n")
