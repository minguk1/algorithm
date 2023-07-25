def perm(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


def perm2(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = A[j]
                used[j] = 1
                perm(i+1, k)
                used[j] = 0

A = [1, 4, 5]
used = [0, 0, 0]


p = [1, 2, 3]
perm(0, 3)
perm2(0, 3)
