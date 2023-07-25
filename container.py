T = int(input())
for tc in range(1, T+1):


    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    new_c = sorted(container)
    new_t = sorted(truck, reverse=True)

    # print(new_c)
    # print(new_t)
    result = []
    skip = False
    for i in new_t:
        # if skip == True:
        #     skip = False
        #     continue
        for j in range(n-1, -1, -1):
            # print(j)
            if i >= new_c[j]:
                result.append(new_c.pop(j))
                n -= 1
                # print(i, result)
                skip = True
                break


    # print(result)
    print(f"#{tc} {sum(result)}")