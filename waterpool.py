T = int(input())
for tc in range(1, T+1):


    price = list(map(int, input().split()))

    month = [0] + list(map(int, input().split()))

    min_price = price[3]

    def select(m, end, total):
        global min_price
        if total > min_price:
            return

        # 종료조건
        if m > end:
            # print(total)
            if total < min_price:
                min_price = total
            return

        # 1일씩
        select(m+1, end, total + month[m]*price[0])
        # 1달씩
        select(m+1, end, total + price[1])
        # 3달씩
        select(m+3, end, total + price[2])

    select(1, 12, 0)
    print(f"#{tc} {min_price}")
