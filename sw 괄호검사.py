T = int(input())
for tc in range(1, T+1):

    a = input()

    stack = []
    result = 1
    for i in a:
        if i  == "(":
            stack.append(i)



        elif i == "{":
            stack.append(i)


        elif i == ")":
            if len(stack) == 0:

                result = 0

                break
            b = stack.pop()

            if not (b == "(" and i == ")"):
                result = 0
                break
        elif i == "}":
            if len(stack) == 0:
                result = 0
                break
            b = stack.pop()

            if not (b == "{" and i == "}"):
                result = 0
                break

    if len(stack) != 0:
        result = 0

    print(f"#{tc} {result}")