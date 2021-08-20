"""
	변수(variable)
		- 변수(variable): 변하는 값
		- 상수(constant): 변하지 않는 값
"""
a = 10  # a: 변수, 10: 상수
b = 10
print(a + b)

a = 30
print(a + b)


"""
	변수 실습하기 
		- 형식: print(출력할 내용)
"""
a = "Hello World"
print(a)

# print(a + 10)  문자열과 숫자는 같이 연산할 수 없다.
print(20 + 30)  # 숫자와 숫자는 연산이 가능하다.
print("Hello " + "World")  # 문자열과 문자열도 연산이 가능하다.

a = 50  # a라는 변수에 50이라는 숫자를 할당
b = 50

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(5 // 2)
print(5 % 2)


"""
	실습
"""
a = 1739583
b = 389344

print(a + b)
print(a - b)
print(a * b)
print(a / b)


"""
	사용자에게 내용을 입력 받으려면?
"""
a = input("데이터를 넣어주세요.")
print(a)


a = int(input("a: "))
b = int(input("b: "))
print(a + b)


"""
	실습: a와 b를 입력 받아 사칙연산의 결과를 출력하는 프로그램 작성
"""
a = input("성을 입력하세요: ")
b = input("이름을 입력하세요: ")
print(f"내 이름: {a+b}")