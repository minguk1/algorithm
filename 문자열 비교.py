T = int(input())
for ts in range(1, T+1):
    in_str = input()
    out_str = input()

    if in_str in out_str:
        print(f"#{ts} 1")
    else:
        print(f"#{ts} 0")