T = int(input())
for ts in range(1, T+1):
    str1_list = list(input())
    str2_list = list(input())
    max_value = 0
    for k in str1_list:
        if str2_list.count(k) >= max_value:
            max_value = str2_list.count(k)
    print(f"#{ts} {max_value}")