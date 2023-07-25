
T = int(input())
for ts in range(1, T+1):
    K, N, M = map(int, input().split())
    m_list = list(map(int,input().split()))
    m_list.append(N)
    if_value = 0
    for i in range(0, M-1):
        if m_list[i+1] - m_list[i] > K:
            if_value += 1
            break
    if if_value >= 1:
        print(f"#{ts} 0")
    else:

        charge_num = 0
        now = 0
        while True:
            now = now + K
            for a in range(0,len(m_list)):
                if now >= m_list[a]:
                    pass
                elif now < m_list[a]:
                    now = m_list[a-1]
                    charge_num += 1
                    # print(now)
                    break
            if now >= N:
                print(f"#{ts} {charge_num}")
                break


