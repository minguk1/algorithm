T = int(input())
for tc in range(1, T+1):

    n = int(input())

    price = [0] * n
    for i in range(n):
        price[i] = list(map(int, input().split()))
    j_list = []

    min_price = 1500
    def select(i, s):
        global min_price


        if s > min_price:
            return


        if i == n:
            if s < min_price:
                min_price = s
                # print(s)
            # print(j_list)
            # print(price_list)
            return

        for j in range(n):
            if j not in j_list:

                j_list.append(j)

                select(i+1, s + price[i][j] )
                j_list.pop()


    select(0, 0)

    print(f"#{tc} {min_price}")