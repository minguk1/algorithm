n = int(input())

base = [0]*1001
for i in range(n):
    a, b = map(int, input().split())
    base[a] = b
print(base)
height1 = [0] * 1002
height2 = [0] * 1002

for i in range(1, 1001):
    if base[i] > height1[i-1]:
        height1[i] = base[i]
    else:
        height1[i] = height1[i-1]
print(height1)
for i in range(1000, 0, -1):
    # print(i)
    if base[i] > height2[i+1]:
        height2[i] = base[i]
    else:
        height2[i] = height2[i+1]
print(height2)
result = [0]*(1002)
for i in range(1002):
    if height1[i] >= height2[i]:
        result[i] = height2[i]
    else:
        result[i] = height1[i]

print(result)
print(sum(result))