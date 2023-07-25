import math
a = int(input())
x = (-1 + (8*a + 1)**0.5)/2
#n층까지 개수의 합이 (n^2+n)/2 인 점을 이용하여
#계산한다음 올림하여 몇 층인지 알아봅니다.

# print(math.ceil(x)) #층이 맞는지 확인
n = math.ceil(x)

stair_sum = n + 1 #층마다 분자와 분모의 합은 sum이 된다.
k = n*(n-1)/2 #이전 층 마지막 항의 번호입니다.
# print(k)
i = a - k #구해야할 번호에서 이전층 마지막 항번호를 빼서 그 층에서
#몇번째인지 알아냅니다.
if n % 2 == 1:
    print(f"{int(n+1-i)}/{int(i)}")
else:
    print(f"{int(i)}/{int(n + 1 - i)}")