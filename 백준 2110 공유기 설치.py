# 붙어 있는 최소 거리를 최대가 되게 배치
n, m = map(int, input().split())

home = [0] * n
for i in range(n):
    home[i] = int(input())
home = sorted(home)

wifi = [0] * m

# 설치 경우에 따라 리셋되는 최대 거리
maximum_dis = 0

def inst(wifi, min_value, cnt, idx):
    global maximum_dis
    # print(wifi)
    # 꼬리 자르기 : 현재 저장되어 있는 인접한 거리의 최소값이 저장된 최대값보다 작다면 어차피 끝까지 가봤자 안되니 종료
    if min_value < maximum_dis:
        return

    if cnt == m:
        print(wifi)
        if maximum_dis < min_value:
            maximum_dis = min_value
            print(maximum_dis)
        return
    if idx == n and cnt != m:
        return
    # wifi 리스트 첫 값 등록할 때
    if cnt == 0:
        # 등록 안하고 넘겨주기
        inst(wifi, min_value, cnt, idx+1)

        # 리스트 인덱스에 등록하고 넘겨주기
        wifi[cnt] = home[idx]

        inst(wifi, min_value, cnt+1, idx+1)
    # wifi 리스트 두번째 값 등록하면 첫번째 두번째값 차를 최솟값으로 보내주기
    elif cnt == 1:
        # 등록 안하고 넘겨주기
        inst(wifi, min_value, cnt, idx + 1)

        # 리스트 인덱스에 등록하고 넘겨주기
        wifi[cnt] = home[idx]

        inst(wifi, wifi[1]-wifi[0], cnt + 1, idx + 1)

    # wifi 리스트 세번째 값 있을 때 이제 비교 시작
    else:
        inst(wifi, min_value, cnt, idx + 1)

        wifi[cnt] = home[idx]
        min_value = min(min_value, wifi[cnt]-wifi[cnt-1])
        inst(wifi, min_value, cnt+1, idx+1)

        # if wifi[cnt]-wifi[cnt-1] < min:
        #     min = wifi[cnt] - wifi[cnt-1]
        # 등록 안하고 넘겨주기

        # 등록 안하고 넘겨주기

# def install(cnt, min, now_idx, pre_idx):
#     global maximum_dis
#     # print(cnt, min, home[now_idx], home[pre_idx])
#     next_dis = 999999999999
#     if now_idx == n and cnt != m:
#         return
#     if cnt == m:
#         if maximum_dis < min:
#
#             maximum_dis = min
#         print('maximum', maximum_dis)
#         return
#
#     else:
#         # 선택했을 때
#
#         if (home[now_idx]-home[pre_idx]) < min:
#             min = home[now_idx]-home[pre_idx]
#
#         install(cnt+1, min, now_idx+1, pre_idx+1)
#         # 선택안하고 넘어갈 때
#         install(cnt, min, now_idx+1, pre_idx)

# install(0, 9999999, 1, 0)
inst(wifi, 9999, 0, 0)
print(maximum_dis)