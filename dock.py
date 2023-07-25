T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    total = []
    for i in range(n):
        a, b = map(int, input().split())

        total.append((a, b))

    total = sorted(total, key=lambda x: x[0])

    result = sorted(total, key=lambda x: x[1])

    end = cnt = 0
    for i, j in result:
        if i >= end:
            cnt += 1
            end = j
    print(f"#{tc} {cnt}")
