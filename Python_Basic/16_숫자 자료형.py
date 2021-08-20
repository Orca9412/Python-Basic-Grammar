# 정수형
a = 10
b = 25
print(a + b)

b = 25.3
print(a + b)  # 35.3 -> 정수형과 실수형 중 더 넓은 개념인 실수형으로 형변환되어 출력된다.


# 16진수 형태 처리 방법: 0x
a = 0xFFFFFFFF
print(a)  # 4294967295 (4비트 * 8 = 32비트)


# 사칙연산
a = 9
b = 7
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b)  # 몫
print("a % b = ", a % b)  # 나머지

# 복소수 연산도 가능
a = (1 + 2j)
b = (3 + 4j)
print(a * b)  # (-5+10j)


