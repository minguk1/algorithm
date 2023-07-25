T = int(input())
for tc in range(1, T+1):

    n, m = map(int, input().split())
    p = [0] * ( n + 1 )

    def make_set(x):
        p[x] = x

    for i in range(1, n+1):
        make_set(i)

    def find_set(x):

        if x == p[x]:
            return x
        else:

            return find_set(p[x])

    def union(x, y):
        p[find_set(y)] = find_set(x)

    lst = list(map(int, input().split()))

    for i in range(0, len(lst)-1, 2):
        # print(lst[i], lst[i+1])
        union(lst[i], lst[i+1])

    # print(p)
    root = []
    for i in range(1, n+1):
        root.append(find_set(i))
    # print(set(root))
    print(f"#{tc} {len(set(root))}")
