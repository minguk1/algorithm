T = int(input())
paper_space = [[0]*10 for i in range(10)]


for i in range(T):
    a, b = map(int, input().split())
    for x in range(a, a+3):
        for y in range(b, b+3):
            paper_space[x][y] += 1
print(paper_space)

count = 0
for i in range(0, 10):
    count = count + paper_space[i].count(0)
print(count)