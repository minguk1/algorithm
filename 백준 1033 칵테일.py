n = int(input())

cock = [0] * n
part = [0] * n
for i in range(n-1):
    a, b, c, d = map(int, input().split())

    if cock[a] == cock[b] == 0:
        cock[a] = c
        cock[b] = d
        part[a] = i+1
        part[b] = i+1
    elif cock[a] == 0 and cock[b] != 0:
        q = part[b]
        for j in range(n):
            if q == part[j] != 0:
                cock[j] = cock[j] * d
                part[j] = i+1
        cock[a] = c * cock[b] // d
        part[a] = i+1

    elif cock[b] == 0 and cock[a] != 0:
        p = part[a]
        for j in range(n):
            if p == part[j] != 0:
                cock[j] = cock[j] * c
                part[j] = i+1
        cock[b] = d * cock[a] // c
        part[b] = i+1
    else:
        s = cock[a]
        t = cock[b]
        p = part[a]
        q = part[b]
        for j in range(n):
            if p == part[j] != 0:
                cock[j] = cock[j] * c * t
                part[j] = i+1
        for j in range(n):
            if q == part[j] != 0:
                cock[j] = cock[j] * d * s
                part[j] = i+1

    # print(cock)
    # print(part)

min_value = min(cock)
div = 2

while True:
    division = True
    for k in cock:
        if k % div == 0:
            continue
        else:
            division = False
            break

    if division == True:
        for j in range(n):
            cock[j] = cock[j] // div
    else:
        div += 1

    if div > min_value:
        break

# print(cock)
for co in cock:
    print(co, end=" ")