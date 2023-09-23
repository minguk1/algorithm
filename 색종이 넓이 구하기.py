T = int(input())
x_start_list = []
y_start_list = []
for i in range(1, T+1):
    x, y = map(int, input().split())
    x_start_list.append(x)
    y_start_list.append(y)

print(x_start_list, y_start_list)

for i in range(1, T+1):
