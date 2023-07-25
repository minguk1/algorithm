T = int(input())

for tc in range(1, T+1):
    a, b = input().split()

    typing = 0

    idx = 0
    while idx < len(a) -len(b) + 1:
        sub = ""
        for i in range(len(b)):
            sub += a[idx + i]

        if sub == b:
            typing += 1
            idx += len(b)

        #패턴 불일치
        else:
            typing += 1
            idx += 1

    while idx < len(a):
        typing += 1
        idx += 1

    print(f"#{tc} {typing}")