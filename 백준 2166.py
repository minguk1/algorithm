n = int(input())
repeat = n - 2

dot_list = []
for i in range(n):
    dot_list.append(list(map(int, input().split())))

# print(dot_list)
x_sum = 0
y_sum = 0
for i in range(n):
    x_sum += dot_list[i][0]
    y_sum += dot_list[i][1]
# print(x_sum, y_sum)

a = x_sum/n
b = y_sum/n
print(a, b)
dot_list = dot_list + [dot_list[0]]
# print(dot_list)
print(round(5.121331, 2))

scale_sum = 0
for k in range(n):

    c = dot_list[k][0]
    d = dot_list[k][1]
    e = dot_list[k+1][0]
    f = dot_list[k+1][1]
    # print(k, a, b, c, d, e, f)
    scale = 0.5*abs((a*d+c*f+e*b)-(b*c+d*e+a*f))
    scale_sum += scale
result = round(scale_sum, 1)
print(scale_sum)
print(result)
