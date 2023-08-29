n = int(input())
n_list = list(map(int, input().split()))
n_list = sorted(n_list)
m = int(input())
m_list = list(map(int, input().split()))


cnt_dict = {}

for n in n_list:
    if n in cnt_dict:
        cnt_dict[n] += 1
    else:
        cnt_dict[n] = 1

for m in m_list:
    if m in cnt_dict:
        print(cnt_dict[m], end=" ")
    else:
        print(0, end=" ")



# cnt_list = [0] * m
# for i in range(m):
#     cnt = 0
#     a = 0
#     b = n-1
#
#     while a != b:
#
#         mid = (a+b)//2
#
#         if n_list[mid] > m_list[i]:
#             b = mid
#         elif n_list[mid] < m_list[i]:
#             a = mid+1
#         elif n_list[mid] == m_list[i]:
#             cnt += 1
#             incre = 0
#             while True:
#
#
#                 incre += 1
#                 if mid+incre<=b and n_list[mid+incre] == m_list[i]:
#                     cnt += 1
#                 else:
#                     break
#             decre = 0
#             while True:
#                 decre += 1
#                 if mid-decre>=a and n_list[mid-decre] == m_list[i]:
#                     cnt += 1
#                 else:
#                     break
#             break
#
#     cnt_list[i] = cnt
#
#
# for t in cnt_list:
#     print(t, end=" ")
