'''
분할 알고리즘
호어 or 로무토
호어가 더 좋다(swap이 더 적게 일어난다.)
'''
def partition(A, l, r):
    # 피봇 정하기 : 제일 왼쪽 원소
    p = A[l]
    # 피봇보다 작은 거는 맨왼쪽으로, 큰 거는 맨오른쪽으로 위치
    i, j = l, r
    # i가 왼쪽에 있으면 안되는 친구의 위치(피봇보다 큰거)
    # j가 오른쪽에 있으면 안되는 친구의 위치(피봇보다 작은거)
    while i <= j:
        # 피봇보다 큰 거를 왼쪽부터 찾기 시작
        while i <= j and A[i] <= p:
            # 현재 i 위치에 있는게 피봇보다 작으면 큰 거를 찾아서 한칸 뒤로 이동
            # 피봇보다 큰 것이 있다면 탐색 중단
            i += 1
        # 피봇보다 작은 거를 오른쪽부터 찾기 시작
        while i <= j and A[j] >= p:
            # 현재 j 위치에 있는게 피봇보다 크면 작은 거를 찾아서 한칸 앞으로 이동
            # 피봇보다 작은 것이 있다면 탐색 중단
            j -= 1

        # 큰 게 왼쪽에 있으면 안되고, 작은 게 오른쪽에 있으면 안되니까 자리 교환
        if i < j:
            A[i], A[j] = A[j], A[i]

    # 반복이 끝나면 작은 것과 큰 것이 다 제자리에 있다. 피봇 위치를 정해준다.
    A[l], A[j] = A[j], A[l]

    # 피봇의 위치를 리턴
    return j

def quicksort(A, l, r):
    if l < r :
        # 분할하고 피봇의 위치를 구한다.
        s = partition(A, l, r)

        # 피봇위치를 정했으니 피봇 제외 왼쪽 정렬
        quicksort(A, l, s-1)
        # 오른쪽 정렬
        quicksort(A, s+1, r)


A = [7, 2, 5, 3, 1, 4, 1]
N = len(A)
quicksort(A, 0, N-1)
print(A)