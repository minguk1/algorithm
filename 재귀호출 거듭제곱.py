for i in range(10):


    tc = input()
    n, m = map(int, input().split())

    def involution(n, m):
        if m == 1:
            return n

        return n * involution(n, m-1)

    print(f"#{tc} {involution(n,m)}")
