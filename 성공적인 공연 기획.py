T = int(input())
for tc in range(1, T+1):

    people = list(input())

    i = 0
    cnt = 0
    minus_sum = 0

    while True:
        if cnt >= i:
            cnt += int(people[i])
            i += 1
        else:
            minus = i - cnt
            minus_sum += minus
            cnt = i
        if i == len(people):
            break

    print(f"#{tc} {minus_sum}")