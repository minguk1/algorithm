n, k = map(int, input().split())
num_list = [str(i) for i in range(1, n+1)]

start = 0
plus = k
length = len(num_list)
result_list = []
while num_list:
    if start + plus -1 >= length:

        t = num_list.pop((start + plus - 1) % length)
        start = (start + plus - 1) % length
        length = len(num_list)
    else:
        # print(start, plus, length)
        t = num_list.pop(start + plus -1)
        start = start + plus -1
        length = len(num_list)
    result_list.append(t)

print(f"<{', '.join(result_list)}>")