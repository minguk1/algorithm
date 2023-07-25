T = 10


def inorder(t):
    if t:
        inorder(left[t])
        print(str_list[t], end="")
        inorder(right[t])

for tc in range(1, T+1):

    n = int(input())
    idx = []
    left = [0]*(n+1)
    right = [0]*(n+1)
    str_list = [""]*(n+1)
    for i in range(n):
        a, b, *c = input().split()

        idx.append(int(a))
        str_list[int(a)] = b
        if len(c) >= 1:
            left[int(a)]= int(c[0])
            if len(c) == 2:
                right[int(a)]= int(c[1])
    # print(idx, left, right, str_list)



    print(f"#{tc}", end=" ")
    inorder(1)
    print()
