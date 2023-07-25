T = int(input())
a = list(map(int, input().split()))

def Bubble(a, T):
    for i in range(T-1, 0 , -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


print(Bubble(a, T))