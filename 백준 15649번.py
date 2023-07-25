n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]


def perm(i, selected):
    if i == m:
        for k in range(m):
            print(selected[k], end=" ")
        print()
        return

    for j in range(n):
        if num_list[j] not in selected:
            selected[i] = num_list[j]
            perm(i+1, selected)
            selected[i] = 0

perm(0, [0]*m)