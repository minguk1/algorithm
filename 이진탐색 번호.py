T = int(input())
for tc in range(1, T+1):

    n = int(input())

    number = [i for i in range(1, n+1)]
    left = [0] * (n+1)
    right = [0] * (n+1)
    i = 1
    while True:
        left[i] = 2*i
        if 2*i == n:
            break
        right[i] = 2 * i + 1
        if 2*i+1 == n:
            break
        i += 1


    # print(left)
    # print(right)
    cnt = 0
    # print(f"#{tc}", end=" ")
    result1 = 0
    result2 = 0

    def preorder(t):
        global cnt, result1, result2
        if t:
            preorder(left[t])
            cnt += 1
            if t == 1:
                result1 = cnt
                # print(cnt, end=" ")
            if t == n//2:
                result2 = cnt
                # print(cnt, end=" ")
            # print(cnt, t)
            preorder(right[t])

    preorder(1)
    print(f"#{tc} {result1} {result2}")
    # print()
    # print()