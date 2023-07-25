#최대 공약수 Greatest Common Divisor
#최소 공배수 Least Common Multilpe
#a > b

def gcd(a, b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def new_gcd(a, b):
    # a % b == 0 이면 b가 최대공약수, 아니면 나머지로 다시 구하기
    if b == 0:
        return a
    else:
        return new_gcd(b, a% b)

print(new_gcd(28, 21))


print(gcd(28, 21))

def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(28, 21))

#소수 구하기
#prime number

#1부터 1000까지 소수 출력
#에라토스테네스의 체
'''
1. 2부터 소스를 구하고자 하는 구간의 모든 수를 나열
2. 2는 소수이므로 2는 소수로 체크하고, 2를 제외한 자기 자신의 배수를 모두 소수가 아니라고 체크
3. 다음 수로 이동(체크 안된 수로), 3은 소수이므로 소수 체크, 3을 제외한 자신의 배수 소수 아니라고 체크
4. 위의 과정 반복
'''
prime = []
for i in range(2, 1000):
    #i를 기준으로 해서 i를 j로 나눴을 때 나머지가 0이면 배수 > 체크
    #j의 범위는 2 <= j < i
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

n = 1000
is_prime = [True for i in range(n+1)] #처음엔 모든 수가 소수라고 생각
for i in range(2, int(n**0.5)+1): #2부터 n의 제곱근까지만 확인해도 된다.
    if is_prime[i]: #i가 소수인 경우
        #i를 제외한 모든 i의 배수를 지우면 된다.
        j = 2
        while i*j <= n:
            is_prime[i*j] = False
            j += 1

print(prime)
print(is_prime) #2부터 체크

