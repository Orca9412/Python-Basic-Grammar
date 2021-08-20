# input() 함수: 사용자로부터 입력을 받아서 문자열 형태로 반환
# print() 함수: 입력받은 값을 출력함.
# a = input()
# print(a)


# 콘솔 계산기 만들기
# 3 7 <- 입력
# 3 + 7 = 10 <- 출력
a = input().split(' ')
# a = ['3', '7']
x = int(a[0])  # 입력받은 수를 정수형으로 형변환
y = int(a[1])
# x와 y에 각각 특정한 수가 담겨 있게 됨.
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)