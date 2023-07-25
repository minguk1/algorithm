T = 10
for tc in range(1, T+1):
    a = input()
    str_list = list(input())
        # print(str_list)
    postfix = ""
    stack = [""]
    i = 0
    while True:
        if "0" <= str_list[i] <= "9":
            postfix += str_list[i]

            i += 1
        else:
            if str_list[i] == "+":

                postfix += stack.pop()
                stack.append("+")
                i += 1
            else:
                postfix += str_list[i+1]
                postfix += str_list[i]

                i += 2
        if i > len(str_list) - 1 :

            # print(str_list[-1])
            # print(stack)
            postfix += stack.pop()
            break
        if i == len(str_list) - 1:
            # print(str_list[-1])
            postfix += str_list[-1]
            postfix += stack.pop()
            break

    # print(postfix)
    str_stack = []
    for i in range(len(postfix)):
        if "0" <= postfix[i] <= "9":
            str_stack.append(int(postfix[i]))
        else:
            if postfix[i] == "*":

                right_num = str_stack.pop()
                left_num = str_stack.pop()
                multi = right_num * left_num
                str_stack.append(multi)
                # print(str_stack)
            else:
                right_num = str_stack.pop()
                left_num = str_stack.pop()
                sum = right_num + left_num
                str_stack.append(sum)
                # print(str_stack)
    # print(postfix[len(postfix)-1])
    print(f"#{tc} {str_stack[0]}")