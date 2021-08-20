# 문자열 자료형 뒤집기: 슬라이싱 사용
str = "Hello World"
print(str[::-1])  # dlroW olleH


# len(): 문자열의 길이를 출력
print(len(str))  # 11 (공백 포함)


# isalpha(): 특정한 문자열이 문자로만 이루어져 있는지 확인
print(str.isalpha())  # False (공백은 해당 x)
str = "HelloWorld"
print(str.isalpha())  # True


# isdigit(): 특정한 문자열이 숫자로만 이루어져 있는지 확인
str = '123123'
print(str.isdigit())  # True (공백은 해당 x)


# isalnum(): 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
str = 'abc123'
print(str.isalnum())  # True (공백은 해당 x)


# join(리스트 자료형): 여러 개의 문자열을 구분자와 함께 합치는 함수
list = ['Hello', 'World', '홍길동']
print(','.join(list))  # Hello,World,홍길동


# sorted(문자열 자료형): 각 문자를 정렬하는 함수 (오름차순)
str = 'helloworld'
list = sorted(str)
print(list)  # ['d', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(''.join(list))  # dehllloorw
list = sorted(str, reverse=True)  # 내림차순 정렬: reverse=True 속성 사용
print(''.join(list))  # wroolllhed


# split(토큰): 문자열을 토큰에 따라서 분리하는 함수
str = 'I wanna watch a moive'
list = str.split(' ')
print(list)  # ['I', 'wanna', 'watch', 'a', 'moive']


# find(sub 문자열): sub 문자열 찾아서 인덱스 반환
str = "I like you"
print(str.find('like'))  # 2
print(str.find('we'))  # -1 (문자열이 포함되어 있지 않다면 -1 반환)

# sub 문자열이 여러 번 들어가는 경우, 가장 앞쪽의 인덱스를 반환
# 두 번째 매개변수에 인덱스를 사용해 해결
str = "I like you like me don't you?"
print(str.find('like', 5))  # 11 (인덱스 5 이후의 like를 찾겠다.)


# upper(), lower(): 문자열을 대문자로 혹은 소문자로 변환해주는 함수
str = "Hello World"
print(str.upper())  # HELLO WORLD
print(str.lower())  # hello world


# strip(): 좌우로 특정한 문자열을 제거하는 함수
str = "     Hello World     "
print(str.strip())  # Hello World (양쪽 공백 제거)
print(str.lstrip())  # 왼쪽 공백 제거
print(str.rstrip())  # 오른쪽 공백 제거

# 매개변수로 문자열을 넣으면, 그 문자열만 제거한다.
str = "ttHello Worldtt"
print(str.strip('t'))  # Hello World


# eval(): 문자열 수식을 계산해주는 함수
exp = "(203+705) * 3 - (30/6)"
print(eval(exp))  # 2719.0
