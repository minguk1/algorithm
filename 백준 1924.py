def days(x):
    if (x == 1) or (x == 3) or (x == 5) or (x == 7) or (x == 8) or (x == 10) or (x == 12):
        return 31
    elif x == 2:
        return 28
    else:
        return 30

m, d = map(int, input().split())

if m >= 2:
    for i in range(1, m):
        d += days(i)

result = d % 7


ddd = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}
print(ddd[result])