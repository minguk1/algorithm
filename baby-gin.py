'''
4
124783
667767
054060
101123
'''
T = int(input())
for tc in range(1, T+1):
    result = False
    number = list(input())
    # print(number)
    number_list = []
    for num in number:
        number_list.append(int(num))

    number_set = set(number_list)
    # print(number_set)

    # triple이 2쌍 있는 경우
    if len(number_set) == 1 or len(number_set) == 2:
        result = True

    else:
        final_list = sorted(number_list)
        # print(final_list)

        for i in range(4):
            #triple 한쌍이 있는 경우
            if final_list[i] == final_list[i+1] == final_list[i+2]:
                a = final_list.pop(i+2)
                a = final_list.pop(i + 1)
                a = final_list.pop(i)
                # print(a)
                # print(final_list)
                # 나머지 3개가 run일 경우
                if final_list[1] - final_list[0] == 1 and final_list[2] - final_list[1] == 1:
                    result = True
                break
        #triple 한쌍도 없는 경우
        if result == False:
            if final_list[1] - final_list[0] == 1 and final_list[2] - final_list[1] == 1 and final_list[4] - final_list[3] == 1 and final_list[5] - final_list[4] == 1:
                result = True

    if result == True:
        print("babygin")
    else:
        print("XXXXX")