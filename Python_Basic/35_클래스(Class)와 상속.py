# 클래스: 객체 지향 프로그래밍이 가능하도록 해주는 가장 기본 단위
"""
	클래스(Class)
		반복되는 불필요한 소스코드를 최소화 하면서
		현실 세계의 사물을 컴퓨터 프로그래밍 상에서
		쉽게 표현할 수 있도록 해주는 프로그래밍 기술
"""
# 인스턴스: 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버: 클래스 내부에 포함되는 변수
# 클래스의 함수: 클래스 내부에 포함되는 함수. 메서드라고 부른다.


class Car:
	# 클래스의 생성자
	# self: 클래스를 이용하여 생성된 인스턴스 그 자체를 의미
	def __init__(self, name, color):
		self.name = name   # 클래스의 멤버 변수로 설정
		self.color = color  # 클래스의 멤버 변수로 설정

	# 클래스의 소멸자 (삭제될 때 처리)
	def __del__(self,):
		print("인스턴스를 소멸시킵니다.")

	# 클래스의 메서드
	def show_info(self):
		print("이름", self.name, "/ 색상:", self.color)

	# Setter 메서드
	def set_name(self, name):
		self.name = name  # 인스턴스가 가지고 있는 이름을 set_name 함수의 매개변수로 바꾸겠다.


# 생성자 + 매서드 사용해서 car1 객체에 할당
car1 = Car('소나타', '빨간색')
car1.show_info()  # 이름 소나타 / 색상: 빨간색
print(car1.name, "을(를) 구매했습니다!")  # 클래스의 멤버 변수에 접근할 때는 온점(.)을 찍어서 접근할 수 있다.

# Setter 메서드 사용
car1.set_name('티코')
car1.show_info()

# 인스턴스를 메모리 상에서 할당 해제 => del 키워드
del car1  # 인스턴스를 소멸시킵니다.
# car1.show_info()  # NameError: name 'car1' is not defined


car2 = Car('아반떼', '검은색')
car2.show_info()  # 이름 아반떼 / 색상: 검은색


"""
	상속
		다른 클래스의 멤버 변수와 메서드를 물려 받아 사용하는 기법
		부모와 자식 관계가 존재한다.
			자식 클래스: 부모 클래스를 상속 받은 클래스
"""


# 부모 클래스 정의
class Unit:
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		print(self.name, "이(가) 공격을 수행합니다. [전투력:", self.power, "]")


# unit = Unit("홍길동", 375)
# unit.attack()  # 홍길동 이(가) 공격을 수행합니다. [전투력: 375 ]

# 자식 클래스 정의
class Monster(Unit):
	def __init__(self, name, power, type):
		self.name = name
		self.power = power
		self.type = type

	def show_info(self):
		print(f"몬스터 이름: {self.name} / 몬스터 종류: {self.type}")


monster = Monster("슬라임", 10, "초급")
monster.show_info()
monster.attack()
