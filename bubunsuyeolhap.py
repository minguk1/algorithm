T = int(input())

for tc in range(1, T+1):

    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    def comb(idx, selected):
        global cnt
        if sum(selected) > k:
            return

        # 종료 조건
        if idx == n:
            print(selected)
            if sum(selected) == k:
                cnt += 1

            return

        # 재귀 호출
        # 고르고 진행 하거나
        selected.append(lst[idx])
        comb(idx+1, selected)
        # 안고르고 진행 하거나
        selected.pop()
        comb(idx+1, selected)

    comb(0, [])
    print(f"#{tc} {cnt}")