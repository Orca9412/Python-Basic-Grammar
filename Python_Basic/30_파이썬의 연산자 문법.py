# 증감 연산자: 기존에 사용하던 증가/감소 기능을 짧게 이용
# 축약형 => 증감 연산자
a = 10
a += 10  # a = a + 10 (사칙연산 모두 가능)
print(a)


# 관계 연산자: 두 개의 값을 비교하여 관계
# A == B: A와 B가 같은지 판별 => True, False
# A != B: A와 B가 다른지 판별 => True, False
# A > B: A가 B보다 큰지 판별
# A < B: A가 B보다 작은지 판별
a = 3
b = 7
print(a == b)  # False
print(a != b)  # True
print(a > b)  # False
print(a < b)  # True

a = 'ABC'
b = 'DEF'
print(a == b)  # False
print(a != b)  # True
print(a > b)  # False
print(a < b)  # True => 알파벳 순서


# 논리 연산자: 여러 개의 수식을 논리적으로 연산
# A and B: A와 B가 모두 참인지 판별
# A or B: A 혹은 B가 참인지 판별
# not A: A가 거짓인지 판별
a = True
b = False
print(a and b)  # False
print(a or b)  # True
print(not a)  # False

if 3 > 5 or 7 < 10:  # True
	print("야호!")

