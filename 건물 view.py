T= 10
for t in range(1, T+1):

    n = int(input())

    background = [[] for i in range(n)]



    input_list = list(map(int, input().split()))

    for i in range(n):
        for j in range(input_list[i]):
            background[i].append(1)

    count = 0
    i = 2
    while i <= (n-2):
        for j in range(len(background[i]), 0, -1):
            if (len(background[i-2]) < j) and (len(background[i-1]) < j) and (len(background[i+1]) < j) and (len(background[i+2]) < j):
                count += 1

            else:
                break
        i += 1


    print(f"#{t} {count}")


