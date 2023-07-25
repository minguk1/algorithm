T = int(input())
for tc in range(1, T+1):


    str_list = list(input().split())
    # print(str_list)
    stack = []
    for i in range(len(str_list)):
        if "0" <= str_list[i] <= "9":
            stack.append(int(str_list[i]))
        elif str_list[i] == ".":
            if len(stack) != 1:
                print(f"#{tc} error")
                break
            c = stack.pop()
            print(f"#{tc} {c}")
            break
        else:

            if len(stack) < 2:
                print(f"#{tc} error")
                break
            right_num = stack.pop()

            left_num = stack.pop()
            if str_list[i] == "+":
                result = left_num + right_num
            elif str_list[i] == "-":
                result = left_num - right_num
            elif str_list[i] == "*":
                result = left_num * right_num
            elif str_list[i] == "/":
                result = int(left_num / right_num)
            stack.append(result)