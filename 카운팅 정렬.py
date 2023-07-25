def Counting_sort(A, B, k): #오름차순
    #A : 정렬 대상
    #B : 정렬된 결과
    #C : 카운트 배열
    #k : 정렬 대상 중 최댓값(원소 개수 세주고 자리 정해줌.)

    C = [0]*(k+1)

    for i in range (0, len(A)):
        C[A[i]] += 1

    for i in range (1, len(C)):
        C[i] += C[i-1]

    for i in range (len(B)-1, -1, -1) : # 1 감소시켜줘야 올바른 자리에 넣을 수 있음 #범위 끝에 -1을 해야 0까지 계산 가능
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    return B

A=[1,5,6,8,2,1,1,6]
k = 8
B = [0,0,0,0,0,0,0,0]

print(Counting_sort(A,B,k))

def Counting_sort_dsc(A, B, k): #내림차순
    #A : 정렬 대상
    #B : 정렬된 결과
    #C : 카운트 배열
    #k : 정렬 대상 중 최댓값(원소 개수 세주고 자리 정해줌.)

    C = [0]*(k+1)

    for i in range (0, len(A)):
        C[A[i]] += 1
    print(C)

    for i in range (len(C)-2, -1, -1):
        C[i] += C[i+1]
    print(C)
    for i in range (len(B)-1, -1, -1) : # 1 감소시켜줘야 올바른 자리에 넣을 수 있음 #범위 끝에 -1을 해야 0까지 계산 가능
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    return B
print(Counting_sort_dsc(A,B,k))