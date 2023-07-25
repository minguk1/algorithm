T = int(input())
for tc in range(1, T+1):

    n, q = map(int, input().split())

    boxex = [0] * n

    for i in range(q):
        a, b = map(int, input().split())
        for j in range(a-1, b):
            boxex[j] = i + 1

    print(f"#{tc}", end=" ")
    print(*boxex, end=" ")
    print()