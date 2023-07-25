def dump(a):
    dump_max = 0
    dump_min = 100
    for i in range(len(a)):
        if a[i] > dump_max:
            dump_max = a[i]

        if a[i] < dump_min:
            dump_min = a[i]
    # print(dump_max, dump_min)
    for i in range(len(a)):
        if a[i] == dump_max:

            b = a.pop(i)
            b -= 1
            a.insert(i, b)
            break
    for i in range(len(a)):
        if a[i] == dump_min:
            c = a.pop(i)
            c += 1
            a.insert(i, c)
            break
    return a


T = 10
for ts in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    i = 0
    while i < N:
        dump(a)
        i += 1
    dump_max = 0
    dump_min = 100

    for i in range(len(a)):
        if a[i] > dump_max:
            dump_max = a[i]

        if a[i] < dump_min:
            dump_min = a[i]
    print(f"#{ts} {dump_max - dump_min}")