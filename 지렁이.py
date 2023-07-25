from itertools import combinations
T = int(input())
for tc in range(1, T+1):

    n = int(input())
    space = [0] * n
    total_x = 0
    total_y = 0
    for i in range(n):
        x, y = map(int, input().split())
        total_x += x
        total_y += y
        space[i] = [x, y]

    johap = list(combinations(space, int(n/2)))

    # print(space)
    # print(johap)
    min_sum = 9999999999999999
    for i in johap:
        # print(i[0])
        x_sum = 0
        y_sum = 0
        for j in range(n//2):
            x_sum += i[j][0]
            y_sum += i[j][1]
        final_x = 2*x_sum - total_x
        final_y = 2*y_sum - total_y
        if final_x*final_x+final_y*final_y < min_sum:

            min_sum = final_x*final_x+final_y*final_y
    print(f"#{tc} {min_sum}")
    print(min_sum**0.5)