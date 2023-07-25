def winner(a, b, c):

    if a[b-1] == 1 and a[c-1] == 3:

        return b
    elif a[b-1] == 3 and a[c-1] == 1:
        return c
    else:
        if a[b-1] > a[c-1]:
            return b
        elif a[b-1] < a[c-1]:
            return c
        elif a[b-1] == a[c-1]:
            return min(b, c)


# print(winner(1,2))

# print(a)
def tournament(i, j):

    # 1. 종료조건
    if i == j:
        # print(i, a[i-1])
        return i



    # 2. 재귀 호출
    left = tournament(i, (i+j)//2)
    right = tournament((i+j)//2+1, j)
    # print(winner(a, left, right), left, right)
    return winner(a, left, right)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    print(f"#{tc} {tournament(1, len(a))}")