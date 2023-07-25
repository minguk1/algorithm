T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    cnt = 0
    # print(price)
    sell = 0
    result = 0
    sum = 0
    compare_list = []
    day = 0
    sell_idx = 0
    while day < N:
        for i in range(day, N):
            if price[i] == max(price[day:]):
                sell_idx = i
        if sell_idx == day:
            break

        # print(price[day:sell_idx])
        purchase = 0
        for j in range(day, sell_idx):
            purchase += price[j]
        cnt = len(price[day:sell_idx])
        sell = cnt * price[sell_idx]
        price[i]
        # print(sell)
        result = sell - purchase
        # print(result)
        sum += result
        if sell_idx == N-1:
            break
        else:
            day = sell_idx + 1
    print(f"#{tc} {sum}")














# while i <= N:
#     cnt = 0
#     purchase = 0
#     for k in range(0,i):
#         if price[k] < price[i - 1]:
#             purchase += price[k]
#             cnt += 1
#     print(i, purchase)
#     sell = price[i-1] * cnt
#     print(i, sell)
#     result = sell - purchase
#     print(result)
#     compare_list.append(result)
#     i += 1
# print(compare_list)
# print(max(compare_list))