# 시퀀스(Sequence): 문자열, 리스트, 튜플 등의 인덱스(Index)를 가지는 자료형
string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(string)  # 문자열
print(list)  # 리스트
print(tuple)  # 튜플

# 시퀀스 자료형은 모두 순서를 가지면서, 동일하게 인덱스를 가지고 있는 자료형이다.
# 인덱싱, 슬라이싱 기법 사용 가능
print(string[0:5])
print(list[0:5])
print(tuple[0:5])

# 반복문에서도 사용 가능
list = [1, 2, 3, 4, 5]
print(4 in list)  # True
print(6 in list)  # False
if 3 in list:
	print("3을 포함하고 있습니다.")

# 연산도 가능
string1 = "Hello World"
string2 = "Happy World"
print(string1 + string2)  # Hello WorldHappy World


# len(시퀀스 자료형): 시퀀스 자료형의 길이를 출력하는 함수
string1 = "Hello World"
string2 = "Happy World"
print(len((string1 + string2)))  # 22
