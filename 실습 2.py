# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

# steak = 50000
# vat = steak * 0.15
# including_vat = round(steak * 1.15, 0)
#
# print(f"스테이크 {steak:^10}")
# print(f"+ VAT  {int(vat):^10}")
# print(f"총계 ₩  {int(including_vat):^10}")
#
# # :>len 오른쪽정렬, len만큼 칸 확보
# # :<len 왼쪽정렬, len만큼 칸 확보
# # :^len 가운데정렬, len만큼 칸 확보

todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]
a = input()
b = int(input())
c = (a, b,)

todo.append(c)

print(todo)