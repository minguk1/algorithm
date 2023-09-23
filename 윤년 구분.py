# 입력 예시
# 2015
# 8
# 31

# 출력 예시
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
#중복을 피하기 위해 입력들을 바로 세트 형식으로 받았습니다.
#같은 글자수여도 정렬을 해야하기 때문에 리스트 형식으로 바꿨습니다.
#글자 수를 1부터 최대 글자 수까지 계산하기 위해 최대 글자 수를 구하였습니다.
#글자 수를 1부터 증가시켜 해당하는 단어부터 출력하도록 하였습니다.
import calendar
date_dict = {}

while True:
    year = int(input())
    month = int(input())
    day = int(input())
    if calendar.isleap(year) == False:
        break


calendar.prcal(year, w=0, l=0, c=6, m=3)
if calendar.weekday(year, month, day) == 0:
    print("경고 월요일입니다.")

date_dict["년"] = year
date_dict["월"] = month
date_dict["일"] = day
if calendar.weekday(year, month, day) == 0:
    date_dict["요일"] = "월요일"
elif calendar.weekday(year, month, day) == 1:
    date_dict["요일"] = "화요일"
elif calendar.weekday(year, month, day) == 2:
    date_dict["요일"] = "수요일"
elif calendar.weekday(year, month, day) == 3:
    date_dict["요일"] = "목요일"
elif calendar.weekday(year, month, day) == 4:
    date_dict["요일"] = "금요일"
elif calendar.weekday(year, month, day) == 5:
    date_dict["요일"] = "토요일"
elif calendar.weekday(year, month, day) == 6:
    date_dict["요일"] = "일요일"

print(date_dict)