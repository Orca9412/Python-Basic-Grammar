a = "Hello"
b = "World!"
print(a + " " + b)  # Hello World! <- 문자열 연산
"""
	+ : 연산자
	a, , " ", b : 피 연산자
"""

# 정수형
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)  # %: 모듈러


# 시프트 연산: 비트를 왼쪽 또는 오른쪽으로 미는 역할을 수행
a = 2  # 00000010
"""
	왼쪽으로 시프트를 2만큼 시키는 경우 == 2를 2번 곱한 것과 같다.
		00001000
	오른쪽으로 시프트를 시키는 경우 == 2를 2의 배수만큼 나누는 것과 같다.
"""
print(a << 3)  # 16  00010000 ==2의 3제곱
print(a >> 1)  # 1 : 00000001 == 2의 0제곱
print(a >> 3)  # 0 : 00000000


# 거듭제곱: **
a = 2
b = 10
print(a ** b)


# 할당 연산자: =
a = 3
print(a == 5)  # False
print(a == 3)  # True
