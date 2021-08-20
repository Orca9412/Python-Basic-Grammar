print("안녕, 파이썬!")

# 문자열 안에서 큰따옴표("), 작은따옴표(')를 사용하고 싶은 경우
print("\"안녕\t, 파이썬!\n줄바꿈이 이루어졌습니다.")  # escape 문자


# 문자열은 연산도 가능하다.
a = "안녕"
b = "파이썬!"
print(a + b)
print((a + b) * 5)


# 문자열의 인덱싱 & 슬라이싱
# 인덱싱: 문자열 내부 문자를 하나씩 다루는 것
a = "Hello World"
print(a[0])  # H, 인덱스 0
print(a[7])  # o, 인덱스 7
print(a[-3])  # r, 인덱스 거꾸로 3번째


# 슬라이싱: 문자열을 여러 부분으로 나눈다. 특정 구간에서 문자열을 확인
print(a[2:9])  # llo Wor
print(a[2:])  # llo World
print(a[:-2])  # Hello Wor
print(a[:])  # Hello World


# step 사용 -> 특정 범위에서 문자를 스텝만큼 건너뛰면서 잘라낼 수 있다.
print(a[0:7:2])  # HloW

