
T = int(input())
for ts in range(1, T+1):


    N = int(input())
    A = input()

    for n in range(N, -1, -1):
        if f"{'1'*n}" in A:
            print(f"#{ts} {n}")
            break
        else:
            pass