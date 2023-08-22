a, b, c = map(int, input().split())
water = [a, b, c]
total = []
c_list = []

def pour(x,y,z):
    global total, c_list, a, b, c
    if (x, y, z) in total:
        return
    else:
        total.append((x,y,z))
    # print(x,y,z)
    if z > 0 and x < a:
        # print(1)
        p = min(z, a-x)
        j = x + p
        k = y
        l = z - p
        if j == 0:
            c_list.append(l)

        # print(j,k,l)

        pour(j,k,l)

    if z > 0 and y < b:
        # print(2)
        p = min(z, b-y)
        j = x
        k = y + p
        l = z - p
        if j == 0:
            c_list.append(l)

        # print(j, k, l)

        pour(j, k, l)

    if y > 0 and z < c:
        # print(3)
        p = min(y, c-z)
        j = x
        k = y - p
        l = z + p
        if j == 0:
            c_list.append(l)

        # print(j, k, l)

        pour(j, k, l)


    if y > 0 and x < a:
        # print(4)
        p = min(y, a-x)
        j = x + p
        k = y - p
        l = z
        if j == 0:
            c_list.append(l)

        # print(j, k, l)

        pour(j, k, l)


    if x > 0 and z < c:

        # print(5)
        p = min(x, c-z)
        j = x - p
        k = y
        l = z + p
        if j == 0:
            c_list.append(l)

        # print(j, k, l)

        pour(j, k, l)

    if x > 0 and y < b:
        # print(6)
        p = min(x, b-y)
        j = x - p
        k = y + p
        l = z
        if j == 0:
            c_list.append(l)

        # print(j, k, l)

        pour(j, k, l)

pour(0,0,c)

c_set = set(c_list)
answer = list(c_set)
answer = sorted(answer)
# for t in c_set:
#     print(t, end=" ")
for t in answer:
    print(t, end=" ")