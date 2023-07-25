import math


def fee(time, distance):
    #대여요금 계산
    rental_fee = time//10 * 1200

    #보험료 계산
    insurance_hour = time // 60
    insurance_minuite = time % 60
    if insurance_minuite >= 50:
        insurance_hour += 1

    insurance_fee = insurance_hour*2 * 525

    #주행요금 계산
    if distance <= 100 :
        distance_fee = 170 * distance
    else:
        distance_fee = 170 * 100 + 85 * (distance-100)

    total_fee = rental_fee + insurance_fee + distance_fee

    return math.ceil(total_fee)

print(fee(600, 50))
print(fee(600, 110))