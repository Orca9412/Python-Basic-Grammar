a = "Hello World"
# a[2] = 'A'
# TypeError: 'str' object does not support item assignment

"""
	파이썬에서 문자열은, 특정한 인덱스에 접근해서 값을 바꿀 수 없다.
"""


# 1. replace() 함수: 문자를 대체해서 반환
a.replace("Hello", "Hi")
print(a)  # Hello World
"""
	replace() 함수는 또 다른 값을 생성하는 것이므로, 별도의 변수에 담고
	그 변수를 출력하는 방식으로 해야 한다.
"""
b = a.replace("Hello", "Hi")
print(b)


# 2. count() 함수: 특정한 부분 문자열의 개수를 반환
print(a.count('l'))  # 3


# 3. find() 함수: 특정한 부분 문자열의 위치 반환
print(a.find('Wor'))  # 6
print(a.find('Word'))  # -1  부분 문자열이 존재하지 않으면 -1을 반환한다.


# 4. upper() 함수: 전체 문자열을 대문자로 변경
print(a.upper())  # HELLO WORLD
b = a.upper()
print(b)  # HELLO WORLD


# 5. lower() 함수: 전체 문자열을 소문자로 변경
print(a.lower())  # hello world


# 6. strip() 함수: 특정 문자열을 지워서 반환
b = a.strip("Hello")
print(b)  # World


b = a.strip("World")
print(b)  # Hello


# 7. split() 함수: 하나의 문자열을 여러 개의 문자열로 나누고, 그 결과를 배열 형태로 반환
a = "Hello World! Hi."
b = a.split(" ")
print(b)  # ['Hello', 'World!', 'Hi.'] -> 배열 형태로 반환. 여러 개의 문자열을 하나로 담아서 관리하겠다.


# 8. zfill() 함수: 문자열의 자릿수만큼 나머지를 0으로 채운다.
b = a.zfill(50)
print(b)  # 0000000000000000000000000000000000Hello World! Hi.

# 주로 금액, 게임 점수 등을 처리할 때 사용된다. 출력 전용 함수
a = "70"
b = a.zfill(5)
print(b)  # 00070


# 9. int() 함수: 숫자 형태의 문자열을 숫자형으로 형변환해서 반환
a = "9475"
b = int(a)
print(b + 505)  # 9980

