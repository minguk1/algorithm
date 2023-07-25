#최소 힙

import heapq

hq = []

#기본
for i in range(10):
    heapq.heappush(hq, i)

for i in range(10):
    print(heapq.heappop(hq), end=" ")
print()

# 응용

#숫자를 우선순위로 나타낼 수 있음
heapq.heappush(hq, (4, "4등"))
heapq.heappush(hq, (2, "2등"))
heapq.heappush(hq, (3, "3등"))
heapq.heappush(hq, (1, "1등"))

for i in range(4):
    print(heapq.heappop(hq), end=" ")
print()

#최대 힙
#비교 대상을 - 를 붙여 값이 커질수록 작게 만들어준다.
for i in range(10):
    heapq.heappush(hq, (-i, i))

for i in range(10):
    print(heapq.heappop(hq), end=" ")
print()