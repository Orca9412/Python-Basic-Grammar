# 예외 처리 (Exception Handling)
try:
	print(3 / 2)
except:
	# ZeroDivisionError: division by zero 예외 처리(handling)
	print("0으로는 나눌 수 없습니다.")
else:
	print("예외 없이 성공적으로 실행되었습니다.")
finally:  # 오류 여부와 상관없이 무조건 실행됨
	print("에외 처리를 마칩니다.")


# Exception 클래스의 객체를 사용해서 오류 내용을 보여줄 수 있다.
try:
	print(3 / 0)
except Exception as e:
	print(e)  # division by zero

