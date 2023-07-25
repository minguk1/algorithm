T = int(input())
for ts in range(1, T+1):
    n = int(input())
    input_str = ""
    for i in range(n):
        a, b = input().split()
        input_str = input_str + a*int(b)
    # print(input_str)
    j = 0
    print(f"#{ts}")
    for i in range(len(input_str)):
        print(input_str[i], end="")
        j += 1
        if j == 10:
            print()
            j = 0
    print()