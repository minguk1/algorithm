orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_list = list(orders.split(","))
# print(orders_list)
print(f"총 {len(orders_list)}건")

orders_set = set(orders_list)
menu = list(orders_set)
menu.sort(reverse=1)
print(menu)