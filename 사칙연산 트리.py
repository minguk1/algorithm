T = 10
for tc in range(1, T+1):

    n = int(input())
    symbol_list = [""] * (n+1)
    left = [0] * (n+1)
    right = [0] * (n+1)
    tree = [0] * (n+1)
    for i in range(1, n+1):
        tree[i] = list(input().split())
    # print(tree)

    def calcu(t):
        if len(tree[t]) == 4:
            if tree[t][1] == "+":
                return calcu(int(tree[t][2])) + calcu(int(tree[t][3]))
            elif tree[t][1] == "-":
                return calcu(int(tree[t][2])) - calcu(int(tree[t][3]))
            elif tree[t][1] == "*":
                return calcu(int(tree[t][2])) * calcu(int(tree[t][3]))
            elif tree[t][1] == "/":
                return calcu(int(tree[t][2])) / calcu(int(tree[t][3]))
        elif len(tree[t]) == 2:
            return int(tree[t][1])

        else:
            pass

    print(f"#{tc} {int(round(calcu(1), 0))}")

