T = int(input())
for tc in range(1, T + 1):

    n = int(input())
    t = n**(1/3)
    print(t)
    if abs(round(t) - t) <= 1e-8:
        print(f"#{tc} {int(round(t))}")
    else:
        print(f"#{tc} -1")
