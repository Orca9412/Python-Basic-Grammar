def go():
	print("Hello")
	print("Hello")
	print("Hello")


go()

a = 10


def func(b):
	c = a + b
	return c  # c를 반환


print(func(10))  # 20


"""
	실습: 지역 변수와 전역 변수 구분하기
"""
a = 10


def square():
	b = a * a
	return b


c = 20 + square()
print(c)  # 120
