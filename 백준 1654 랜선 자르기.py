k, n = map(int, input().split())

lans = []
for i in range(k):
    lans.append(int(input()))

a = 1
b = max(lans)

while a <= b:
    mid = (a+b)//2

    lan_sum = 0
    for lan in lans:
        lan_sum += (lan // mid)

    if lan_sum >= n:
        a = mid + 1
    else :
        b = mid - 1

print(b)