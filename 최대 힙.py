import random

heap = [0] * 101

last = 0

def enq(item):

    global last
    last += 1 #마지막 위치에 원소 추가
    heap[last] = item

    #추가를 하고 나서 부모노드가 자식노드보다 큰지 만족하도록 해야한다.

    c = last #자식 위치
    p = c // 2 #완전 이진트리에서 부모 위치 계산

    #부모 노드가 존재하고 자식이 부모보다 작을 때까지 위치 변경

    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        #자리를 바꿨으면 자식의 위치를 또 바꿔준다.

        c = p
        p = c // 2

for i in range(10):
    enq(random.randrange(1, 101))

print(heap)

def deq():
    global last
    #루트 노드 삭제전 기억
    tmp = heap[1]

    #마지막 노드를 삭제해서 루트위치에 땡겨온다.
    heap[1] = heap[last]
    last -= 1
    #마지막 노드 위치 1 감소

    #루트부터 자리 찾기(비교해서 나보다 큰 값이 자식 중에 있으면 자리 교환)
    p = 1
    c = p * 2 #왼쪽 자식을 기준으로 해서
    #자식 위치로 가봤는데 자식이 last보다 작아야 트리 안에 존재
    while c <= last:
        # 만약 오른쪽 자식이 있다면, 둘 중에 큰 자식과 비교를 한다.
        if c+1 <= last and heap[c] < heap[c+1]:
            #비교대상 오른쪽 자식으로 바꿔준다
            c = c + 1

        #자식이 부모보다 크다면 힙에 조건 위배
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        #자식이 부모보다 작다면 반복 종료
        else:
            break

    return tmp

for i in range(10):
    enq(random.randrange(1, 10000))

print(heap)

for i in range(10):
    print(deq())


