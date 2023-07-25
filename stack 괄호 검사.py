def check(a):
    if a.count("(") != a.count(")"):

        return False
    stack = []
    cnt = 0
    for i in range(len(a)):
        if a[i] == "(":
            # cnt += 1
            stack.append(a[i])
            print(stack)

        elif a[i] == ")":
            # cnt -= 1

            if len(stack) == 0:
                print(stack)
                return False
            b = stack.pop()
        # if cnt < 0:
        #     return False

    # if cnt != 0:
    #     return False
    print(stack)
    if len(stack) != 0:
        return False

    return True

a = input()

print(check(a))

def check2(row):
    stack = []
    answer = 1
    for c in row:
        if c == "(":
            stack.append(c)

        if c == ")":
            if len(stack) == 0:
                answer = 0
                break
        b = stack.pop()
        if not (b == "(" and c == ")"):
            answer = 0
            break

    if len(stack) > 0:
        answer = 0
    return answer