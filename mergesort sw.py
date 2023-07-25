T = int(input())
for tc in range(1, T+1):

    n = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    tmp = [0] * n
    def mergesort(left, right):
        global cnt

        if left == right-1:

            return

        mid = (right - left) // 2 + left
        # print(mid)
        # print(A[mid])
        # print(A[right])

        mergesort(left, mid)
        mergesort(mid, right)

        l, r = left, mid
        if A[mid-1] > A[right-1]:
            cnt += 1
            print(cnt, mid, A[left:mid], A[mid:right])
        for k in range(left, right):
            if r >= right:
                tmp[k] = A[l]
                l += 1
            # 오른쪽 부분만 남은 경우 : 오른쪽 배열 남은 거 추가
            elif l >= mid:
                tmp[k] = A[r]
                r += 1
            # 둘다 남아 있는 경우
                    # 왼쪽이 작으면 왼쪽 거 추가
            elif A[l] <= A[r]:
                tmp[k] = A[l]
                l += 1
                    # 오른쪽이 작으면 오른쪽 거 추가
            else:
                tmp[k] = A[r]
                r += 1

        for i in range(left, right):
            A[i] = tmp[i]

    mergesort(0, n)
    # print(A)
    print(f"#{tc} {A[n//2]} {cnt}")