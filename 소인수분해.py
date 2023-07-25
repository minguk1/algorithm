T = int(input())
for ts in range(1, T+1):

    N = int(input())

    soinsu_list = [2, 3, 5, 7, 11]
    result = 0
    print(f"#{ts}", end=" ")
    for i in range(5):

        count = 0
        while True:
            if N % soinsu_list[i] == 0:
                count = count + 1
                N = N // soinsu_list[i]
            else:
                print(count, end=" ")
                break
    print()