T= int(input())
for tc in range(1, T+1):
    n = input()
    a = input()
    a_list = list(a)
    a_dict = {}
    for i in a_list:
        a_dict[int(i)] = a_list.count(i)

    sorted_dict = sorted(a_dict.keys() , reverse=True)


    for i in sorted_dict:
        if a_dict[int(i)] == max(a_dict.values()):
            print(f"#{tc} {int(i)} {max(a_dict.values())}")
            break



