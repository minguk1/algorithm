n = 5

list2 = [[0]*n for _ in range(n)]

print(list2)

now = [2,2]

move = [1, 3, 3]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
x = 2
y = 2
for i in move:
    x = x + dx[i]
    y = y + dy[i]

print(x)
print(y)

del list[x][y]
list[x][y].insert(1)
print(list2)