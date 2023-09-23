T = int(input())
a = list(map(int, input().split()))
b = sorted(a)
c = (len(a)-1) // 2
print(b[c])