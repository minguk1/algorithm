# 내 처음 풀이
# year = int(input())
#
# if year % 400 == 0:
#     year = "윤년"
#
# elif year % 100 == 0:
#     year = "윤년 아님"
# elif year % 4 == 0:
#     year = "윤년"
#
# else:
#     year = "윤년아님"
#
# print(year)

# 교수님 코드
# year = int(input("연도를 입력하세요 : "))
#
# if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0:
#     year = "윤년"
#
# else:
#     year = "윤년 아님"
# print(year)

import calendar
year = int(input())

print(calendar.isleap(year))