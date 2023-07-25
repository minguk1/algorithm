n = int(input())
input_dict = {}
a_list = []
b_list = []

for i in range(6):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    if a in input_dict:
        input_dict[a] = input_dict.get(a,[])+[b]
    else:
        input_dict[a] = [b]

# print(input_dict)
total_space = 1
# print(a_list)
# print(b_list)
b_del_list = []

for i in input_dict:
    if a_list.count(i) == 1:
        total_space = total_space * input_dict[i][0]
# print(total_space)

for i in range(6):
    if a_list.count(a_list[i]) == 1:
        if i-1 < 0:
            b_del_list.append(5)
        if i+1 > 5:
            b_del_list.append(0)
        b_del_list.append(i-1)
        b_del_list.append(i)
        b_del_list.append(i+1)


# print(b_del_list)
b_del_set = set(b_del_list)
# print(b_del_set)
substract_scale = 1

for i in range(6):
    if i in b_del_set:
        pass
    else:
        substract_scale = substract_scale * b_list[i]
        # print(b_list[i])
        # print(b_list[3])
# print(substract_scale)
result = (total_space - substract_scale) * n
print(result)

