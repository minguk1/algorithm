T = 10
for tc in range(1, T+1):
    n, s = input().split()
    n = int(n)
    stack = []

    for i in s:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            c = stack.pop()

    result = ''.join(stack)
    print(f"#{tc} {result}")

    # while True:
    #     if s_list[i] == s_list[i+1]:
    #         b = s_list.pop(i+1)
    #         c = s_list.pop(i)
    #         n -= 2
    #         # print(n)
    #         # print(s_list)
    #         i = 0
    #     else:
    #         i += 1
    #     if i == n-1:
    #         break

    # result = ''.join(s_list)
