T = int(input())
for tc in range(1, T+1):

    n = int(input())
    if n == 1:
        print(f"#{tc} {input()}")
    else:
        farm = [[0] * n for _ in range(n)]
        for i in range(n):
            input_list = list(input())
            for k in range(n):
                farm[i][k] = int(input_list[k])


        start = (n-1)//2
        k = 0
        plant_sum = sum(farm[start])

        while True:
            k += 1
            plant_sum += sum(farm[start+k][k:-k])
            plant_sum += sum(farm[start-k][k:-k])
            if k == (n-1) // 2:
                break
        print(f"#{tc} {plant_sum}")

