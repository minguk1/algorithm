def perm(i, k):
    # 카운트가 다 채워졌다면 출력
    if i == k:
        print(*p)
    else:
        # j를 i(숫자가 정해진 자릿수) 이상부터 끝 자릿수까지 반복
        for j in range(i, k):
            # i번째와 j번째 위치 변경하고 자릿수 더한 재귀 함수 실행
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            # 바꾼 리스트 위치 다시 원래대로 돌리기
            p[i], p[j] = p[j], p[i]


def perm2(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k):
            # 방문 배열과 비슷하게 해당 원소가 채워져 있는지 나타내는 리스트 따로 만들어주기
            # j번째 원소를 안썼다면
            if used[j] == 0:
                # 현재 자릿수에 j번째 원소 넣기
                p[i] = A[j]
                # j번째 원소 사용했다는 표시 남기기
                used[j] = 1
                # 그 상태로 한자리 더해 재귀함수 실행
                perm(i+1, k)
                # 고르지 않고 넘어가는 경우
                used[j] = 0

A = [1, 4, 5]
used = [0, 0, 0]


p = [1, 2, 3]
perm(0, 3)
perm2(0, 3)
