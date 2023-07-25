T = int(input())
for i in range(1, T+1):
    N = int(input())

    won50000 = 0
    won10000 = 0
    won5000 = 0
    won1000 = 0
    won500 = 0
    won100 = 0
    won50 = 0
    won10 = 0

    won50000 += (N // 50000)
    N = N % 50000
    won10000 += (N // 10000)
    N = N % 10000
    won5000 += (N // 5000)
    N = N % 5000
    won1000 += (N // 1000)
    N = N % 1000
    won500 += (N // 500)
    N = N % 500
    won100 += (N // 100)
    N = N % 100
    won50 += (N // 50)
    N = N % 50
    won10 += (N // 10)
    N = N % 10
    print(f"#{i}\n{won50000} {won10000} {won5000} {won1000} {won500} {won100} {won50} {won10}")