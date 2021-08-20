# 첫 명령어는 들여쓰기 없이 시작해야 한다.
# 조건문, 반복문 등의 문법을 사용할 때는 콜론(:)으로 명령어의 끝을 알린다.
# 콜론(:)의 다음 줄부터는 들여쓰기의 간격이 모두 일정해야 한다.

score = 75
if score >= 80:  # True 일 때만,
	print("Good")  # 들여쓰기 된 문이 실행된다.
	print("점수가 80점 이상입니다.")
elif score >= 70:
	print("Not Bad")  # 조건을 연쇄적으로 검사할 때 eilf 사용
	print("점수가 70점 이상입니다.")
else:  # 조건을 만족하지 못하는 경우(False)일 때 else 사용
	print("Bad")
print("어떤 내용")


score = 85
if score < 90 and score >= 80:  # and, or, not 연산자를 사용하는 것이 좋다.
	print("Good")


# 리스트에 특정 원소가 있는지 검사할 때, 조건문(if) 사용
list = [1, 2, 3]
if 2 in list:
	print("2가 리스트에 포함되어 있습니다.")
