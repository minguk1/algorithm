T = int(input())
for ts in range(1, T+1):
    D, A, B, F = map(int, input().split())

    time = D / (A+B)
    fly_distance = time * F
    result = round(fly_distance, 7)
    print(f"#{ts} {result}")