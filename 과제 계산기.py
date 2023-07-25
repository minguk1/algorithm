T = 10
for tc in range(1, T+1):
    a = input()
    str_list = list(input())
        # print(str_list)
    postfix = ""
    stack = []
    i = 0
    while i <= len(str_list)-1:
        if "0" <= str_list[i] <= "9":
            postfix += str_list[i]

            i += 1
        else:
            postfix += str_list[i+1]
            postfix += str_list[i]

            i += 2
    # print(postfix)

    for i in range(len(postfix)):
        if "0" <= postfix[i] <= "9":
            stack.append(int(postfix[i]))
        else:
            right_num = stack.pop()
            left_num = stack.pop()
            sum = right_num + left_num
            stack.append(sum)
    print(f"#{tc} {stack[0]}")