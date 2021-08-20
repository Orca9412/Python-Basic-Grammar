# 함수: 특정한 입력을 받아서 처리를 한 이후에, 특정한 출력을 하는 모듈
# 함수를 이용하면 특정한 소스코드의 반복을 줄일 수 있다는 특징이 있다.

def add(a, b):
	sum = a + b
	return sum


a = add(1, 2)
print(add(1, 2))  # 3
print(a)  # 3


def add2(a, b):
	print(a + b)  # return문 없이 바로 출력


add2(1, 2)  # 3


# 가변 인자: 함수의 매개변수가 가변적일 수 있을 때 사용
def function(*data):  # 매개변수가 어떨 때는 1개였다가, 어땔 때는 2개였다가... * (포인터) 기호를 사용한다.
	print(data)


function(1, 2, 3)


# 전역변수와 지역 변수
# 전역 변수: 소스코드 전체 어디에서든지 사용 가능한 변수
# 지역 변수: 특정한 함수(블록) 안에서만 사용할 수 있는 변수
def add3():
	global a  # 전역 변수 사용
	a += 5  # 지역 변수


a = 2  # 전역 변수
add3()
print(a)  # 7


# 파이썬의 함수는 반환 값이 여러 개일 수 있음
def function():
	a = 5
	b = [1, 2, 3]
	return a, b


a, b = function()
print(a)  # 5
print(b)  # [1, 2, 3]
