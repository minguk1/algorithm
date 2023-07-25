orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
order_list = orders.split(",")
# print(orders.split(","))
# print(type(order_list))
cnt = 0
for order in order_list:
    # print(order[0:3])
    if order[0:3] == '아이스':
        cnt = cnt + 1
        # print(order[0:3])

print(f"아이스 {cnt}건")



orders_set = set(order_list)
# print(orders_set)

for u in orders_set:
    print(u, order_list.count(u))

#다른 방법
orders_dict = {}
for u in order_list:
    if u not in orders_dict:
        orders_dict[u] = 0
    orders_dict[u] += 1

print(orders_dict)