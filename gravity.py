# n = int(input())
# box = list(map(int, input().split()))
#
# ans = 0 #충분히 작은 값으로 초기 최댓값 설정
# for i in range(n):
#     #현재 위치에서 맨 꼭대기 상자가 오른쪽에 장애물이 없다고 했을 때 최대 낙차 구하기
#     h = n - 1 - i
#     #또 반복문을 돌면서 현재 내 위치 기준 오른쪽에 있는 장애물 수 구하기
#     right_num = 0
#     for j in range(i+1, n):
#         if box[j] >= box[i]:
#             right_num += 1
#     #최대 낙차 = 현재 위치에서 오른쪽에 상자가 없을 경우 최대 낙차 - 오른쪽 상자 수
#     max_h = h - right_num
#     #최대 낙차 중 최댓값 갱신
#     if max_h >= ans:
#         ans = max_h
# print(f"{ans}")

a = [2,2,1,1,1,1,2,2,2]
b = ""
for i in a:
    b = b + str(i)

for i in range(len(a)-1): #낮아졌다가 올라갈 때
    if a[i] - a[i+1] > 0: #낮아졌는데
        print(f"{str(a[i+1])*2*2}" == b[i+1:i+1+2*2])