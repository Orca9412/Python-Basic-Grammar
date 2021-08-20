"""
	반복문 (iterative)
		- 조건에 부합하는 한, 특정한 명령어를 반복
"""
# 숫자 범위 표현: range(시작, 끝) 함수를 사용해서, 반복문의 반복 범위를 정할 수 있다.
sum = 0
for i in range(1, 10):
	print(i)
	sum += i
print("합계:", sum)


# 문자열 처리 예제: 특정 문자의 포함횟수 찾기
count = 0
for i in "Hello World":
	if i == 'o':
		count += 1
print("o의 개수는", count, "개 입니다.")


# 리스트 처리 예제: 리스트에 포함되어 있는 정수의 합 구하기
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
	sum += i
print("합계:", sum)


"""
	반복문은 break 문과 continue 문을 함께 사용할 수 있다.
"""
# continue: continue 를 만났을 때, 더 이상 명령어를 실행하지 않고, 다음 반복을 진행한다.
# break: break 를 만나면 반복문을 즉시 벗어난다.
sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
	if i % 2 == 1:  # 홀수일 때
		continue  # 명령어를 실행하지 않고 다음 반복 진행
	elif i % 2 == 0:  # 짝수일 때
		break  # 반복문을 즉시 벗어난다.
	sum += i
print("합계:", sum)  # 0 (홀수일때 continue 되어 다음 원소인 2가 짝수이므로 반복문을 즉시 벗어나기 때문)


"""
	while 문
		- 특정한 조건을 만족할 때, 계속해서 반복을 수행한다.
"""
i = 0
sum = 0
while i <= 5:
	i += 1
	if i % 2 == 1:
		continue
	sum += i
print("합계:", sum)  # 12

