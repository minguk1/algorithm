T = int(input())
for tc in range(1, T+1):


    n, m = map(int, input().split())

    n_list = list(map(int, input().split()))
    n_list = sorted(n_list)
    m_list = list(map(int, input().split()))

    result = []

    def find(x, lst, st, en):

        l = st
        r = en
        m = (l + r)//2

        mid = lst[m]
        if l == r:
            if x != mid:
                result.append((x, False))
                return False

        if x == mid:
            result.append((x, True))
            return True

        else:
            if x > mid:

                direction_list.append(2)
                if direction_list[-1] == direction_list[-2]:
                    result.append((x, False))
                    return False

                find(x, lst, m+1, r)

            else:
                direction_list.append(1)
                if direction_list[-1] == direction_list[-2]:
                    result.append((x, False))
                    return False

                find(x, lst, l, m-1)

    for t in m_list:
        direction_list = [0]
        find(t, n_list, 0, n-1)
    #     print(direction_list)
    #
    # print(result)
    value = 0
    for idx, re in result:
        if re == True:
            value += 1

    print(f"#{tc} {value}")