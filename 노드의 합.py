T= int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())

    node = [0] * (n+1)

    for i in range(m):
        a, b = map(int, input().split())
        node[a] = b
    # print(node)
    def nodesum(t):
        if t <= n and node[t] != 0:
            # print(t, node[t])
            # print(type(node[t]))
            return node[t]

        elif t <= n:

            child_sum = nodesum(t*2) + nodesum(t*2+1)
            return child_sum

        else:
            return 0
    print(f"#{tc} {nodesum(l)}")