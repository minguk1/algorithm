from itertools import combinations

n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = list(map(int, input().split()))

print(arr)

players = [i for i in range(1, n+1)]
print(players)
com = list(combinations(players, n//2))
print(com)

min_value = 9999
for i in range(len(com)//2):
    a = b = 0
    for k in com[i]:
        for j in com[i]:
            if k != j:
                a += arr[k-1][j-1]

    for k in com[-i-1]:
        for j in com[-i-1]:
            if k != j:
                b += arr[k-1][j-1]
    if abs(a-b) < min_value:
        min_value = abs(a-b)
        if min_value == 0:
            break

print(min_value)