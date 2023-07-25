lst = []
for i in range(9):
    lst.append(list(map(int, input().split())))

max_value = 0
a, b = 0, 0
for i in range(9):
    for j in range(9):
        if lst[i][j] > max_value:
            max_value = lst[i][j]
            a, b = i, j

print(max_value)
print(a+1, b+1)