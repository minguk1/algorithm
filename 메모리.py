T = int(input())
for tc in range(1, T+1):

    memory = input()
    # print(memory.find("1"))
    if "1" in memory:
        first = memory.find("1")
        i = first
        cnt = 1
        for i in range(first, len(memory)-1):
            if memory[i] != memory[i+1]:
                cnt += 1
        print(f"#{tc} {cnt}")
    else:
        print(f"{tc} 0")

# T = int(input())
# for tc in range(1, T + 1):
#     ans = 0
#     lst = list(map(int, input()))
#     org = [0] * len(lst)
#     for i in range(len(lst)):
#         if lst[i] != org[i]:
#             n = i
#             while n < len(lst):
#                 org[n] = lst[i]
#                 n += 1
#             ans += 1
#
#     print(f'#{tc} {ans}')