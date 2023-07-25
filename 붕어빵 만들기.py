T = int(input())
for tc in range(1, T+1):


    n, m, k = map(int, input().split())
    client = list(map(int, input().split()))

    result = "Possible"
    t = 0
    b = 0
    boongabbang = 0
    while True:
        if t % m == 0 and t != 0:
            boongabbang += k

        if t in client:
            if boongabbang >= client.count(t):
                boongabbang -= client.count(t)
            else:
                result = "Impossible"
                break
        t += 1
        if t > max(client):
            break

    print(f"#{tc} {result}")
