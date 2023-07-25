T = int(input())
for tc in range(1, T+1):

    n = int(input())
    heap = [0]*(n+1)
    idx = 0
    def enq(a):
        global idx
        idx += 1
        heap[idx] = a

        child = idx
        parent = idx//2

        while parent and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]

            child = parent
            parent = child // 2
    input_list = list(map(int, input().split()))
    for i in range(n):
        enq(input_list[i])

    # print(heap)

    parent_sum = 0
    now = n
    while True:
        pa = now // 2
        if pa == 0:
            break
        else:
            parent_sum += heap[pa]
            now = pa
            # print(parent_sum)
    print(f"#{tc} {parent_sum}")