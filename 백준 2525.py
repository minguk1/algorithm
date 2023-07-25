now_h, now_m = map(int, input().split()) # 현재 시간과 분을 입력으로 받습니다.
need_m = int(input()) # 증가하는 시간을 입력을 받습니다.

sum_m = now_m + need_m #분이 얼마나 증가하는지 계산

plus_h = sum_m // 60 #60분이 넘어갈 때 마다 시간이 1시간씩 증가하므로 몫을 이용


result_h = (now_h + plus_h) % 24 #현재 시간과 몫으로 넘어간 시간을 더하고 24시간 까지 있으니 24의 나머지로 계산
result_m = sum_m % 60 #전에 했던 증가한 분을 60으로 나눠 그 나머지가 현재 분이 됩니다.

print(result_h, result_m) #끝나고 시간과 분 출력