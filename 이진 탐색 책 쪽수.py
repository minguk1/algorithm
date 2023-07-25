T = int(input())
for ts in range(1, T+1):
    N, A, B = map(int, input().split())

    def number_check(b, key):
        start = 1
        end = b
        num = 0
        while True:
            c = int((start+end)/2)
            num += 1
            if c == key:
                return num
                break
            elif key < c:
                end = c
            else:
                start = c
        return num

    player1 = number_check(N, A)
    player2 = number_check(N, B)

    if player1 < player2:
        print(f"#{ts} A")
    elif player1 > player2:
        print(f"#{ts} B")
    else:
        print(f"#{ts} 0")