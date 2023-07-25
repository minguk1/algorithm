T = int(input())
for tc in range(1, T+1):
    s = input()
    s_list = list(s)
    la_index = []

    for i in range(len(s)-1):
        if s[i] == "(" and s[i+1] == ")":
            la_index.append(i)
    for i in la_index:
        s_list[i], s_list[i+1] = "l", "a"

    stack = []
    cnt = 0
    for i in range(len(s_list)):
        if s_list[i] == "(":
            stack.append("(")
        elif s_list[i] == ")":
            t = stack.pop()
            cnt += 1
        elif s_list[i] == "l":
            cnt += len(stack)

    print(f"#{tc} {cnt}")