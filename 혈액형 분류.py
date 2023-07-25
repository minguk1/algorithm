blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
# #
# # blood_set = set(blood_types)
# #
# #
# #
# # blood_list = list(blood_set)
# #
# # blood_list.sort()
# #
# #
# # blood_dict = {}
# #
# # for i in blood_list:
# #     blood_dict[i] = f"{blood_types.count(i)}명"
# #
# # print(blood_dict)

blood_dict = {}

for blood in blood_types:
    if blood_dict.get(blood): # 딕셔너리에 blood 키가 있을 경우
        blood_dict[blood] += 1
    else:
        blood_dict[blood] = 1

print(blood_dict)
