a, b, c = map(int, input().split()) #각 주사위의 변수 설정

if a == b == c:
    prize = 10000+a*1000 #prize라는 상금 변수 설정

elif a == b or b == c or a == c:
    if a == b or a ==c:
        prize = 1000 + a*100
    else:
        prize = 1000 + b*100
else:
    prize = max(a,b,c) * 100

print(prize)