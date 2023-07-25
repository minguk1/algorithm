st_end = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

n = int(input())

number = [0] * n
for i in range(n):
    number[i] = list(map(int, input().split()))
max_sum = 0

for i in range(1, 7):
    visit = [[0]*6 for _ in range(n)]
    now_sum = 0
    k = 0
    bottom = number[0].index(i)

    while True:
        top = st_end[bottom]

        top_number = number[k][top]

        visit[k][bottom] = 1
        visit[k][top] = 1


        k += 1

        if k == n:
            break
        bottom = number[k].index(top_number)

    for i in range(n):
        row_max = 0
        for j in range(6):
            if visit[i][j] == 0 and number[i][j] > row_max:
                row_max = number[i][j]

        now_sum += row_max

    if now_sum > max_sum:
        max_sum = now_sum
print(max_sum)