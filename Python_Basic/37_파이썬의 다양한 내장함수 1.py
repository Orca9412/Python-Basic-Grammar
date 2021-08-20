# input(): 사용자로부터 콘솔로 입력을 받는 함수
# int(): 정수 자료형으로 변환
# user_input = input('정수를 입력하세요: ')
# print(f'제곱: {int(user_input) ** 2}')
a = '12345'
print(int(a))
b = 12.5
print(int(b))  # 소수점 이하는 버린다.


# float(): 문자열, 정수 등의 자료형을 실수형으로 변환
a = 10
print(float(a))  # 10.0


# max(), min(): 시퀀스 자료형에 포함되어 있는 원소 중, 최대값 혹은 최소값 반환
list = [5, 6, 3, 2, 9, 8, 4, 1, 7]
print(max(list))  # 9
print(min(list))  # 1


# bin(), hex(): 10진수를 => 2진수 변환, 10진수 => 16진수를 문자열로 반환
print(bin(128))  # 0b10000000
print(hex(230))  # 0xe6
print(int('0xe6', 16))  # 16진수 => 10진수 (230)


# round(): 반올림 수행
print(round(123.789))  # 124
print(round(123.789, 0))  # 124.0
print(round(123.789, 1))  # 123.8
print(round(123.789, 2))  # 123.79
print(round(123.789, -1))  # 120.0


# type(): 자료형의 종류 반환
int = 1
str = "문자열"
list = [1, 2, 3]
dict = {'apple': "사과"}
print(type(int))  # <class 'int'>
print(type(str))  # <class 'str'>
print(type(list))  # <class 'list'>
print(type(dict))  # <class 'dict'>
