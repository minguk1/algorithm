T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())
    fire_list = [0] * n
    pizza_list = list(map(int, input().split()))
    for i in range(n):
        fire_list[i] = [pizza_list[i], i]
    # print(fire_list)
    last_index = -1
    k = 0
    j = 0
    zero_list = []
    while True:
        # print(fire_list[k][0])

        front = fire_list[k][0] // 2
        # print(front)
        i = fire_list[k][1]
        if front == 0:
            zero_list.append(i)
            if n + j <= m -1:
                fire_list.append([pizza_list[n+j], n+j])
                j += 1
                # print(fire_list)
            k += 1
            pass
        else:
            fire_list.append([front, i])
            # print(fire_list)
            k += 1
        if len(zero_list) == m - 1:
            break
    print(f"#{tc} {fire_list[-1][1]+1}")







# k = 0
# end = False
# while True:
#
#
#     for i in range(len(fire_list)):
#         if fire_list[i] == 0:
#             print(i)
#             fire_list[i] = -1
#             print(fire_list)
#             if n+k <= m-1:
#                 fire_list.append(pizza_list[n+k])
#                 print(fire_list)
#                 k += 1
#             if fire_list.count(-1) == m - 1:
#                 end = True
#                 break
#     for i in range(len(fire_list)):
#         fire_list[i] = fire_list[i] // 2
#     print(fire_list)
#     if end == True:
#         for i in range(len(fire_list)):
#             if fire_list[i] != -1:
#                 print(i)
#         break


