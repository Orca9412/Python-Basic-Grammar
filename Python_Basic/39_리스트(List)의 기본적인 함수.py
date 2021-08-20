# index(원소): 리스트 내 특정한 원소의 인덱스를 찾기
list = ['나동빈', '강종일', '이태일', '박한울', '이상욱']
print(list.index('이태일'))  # 2

# reverse(): 리스트의 원소를 뒤집기
list = [1, 2, 3]
list.reverse()
print(list)  # [3, 2, 1]

# 슬라이싱 기법도 사용 가능: 순서가 있기 때문
list = list[::-1]
print(list[::-1])  # [3, 2, 1]


# sum(리스트 자료형): 리스트의 모든 원소의 합 반환
list = [1, 2, 3]
print(sum(list))  # 6


# range(시작, 끝 -1): 특정 범위를 지정
# list(특정 범위): 특정 범위의 원소를 가지는 리스트를 반환
my_range = range(5, 10)  # 5 ~ 9
my_list = list(my_range)
print(my_list)  # [5, 6, 7, 8, 9]


# all() / any(): 리스트의 모든 원소가 참인지 / 하나라도 참인지 판별하는 함수
list = [True, False, True]
print(all(list))  # False
print(any(list))  # True


# enumerate(): 리스트에서 인덱스와 원소를 함께 추출하여 튜플 형태로 반환
my_list = ['나동빈', '강종구', '이태일', '박한울', '이상욱']
result = list(enumerate(my_list))
print(result)  # [(0, '나동빈'), (1, '강종구'), (2, '이태일'), (3, '박한울'), (4, '이상욱')]

# 반복문에서 사용되는 경우
for i, k in enumerate(my_list):
	print(f"인덱스: {i} / 원소: {k}")


# sort(): 리스트의 원소를 정렬
my_list = ['나동빈', '강종구', '이태일', '박한울', '이상욱', '이태일']
my_list.sort()
print(my_list)  # ['강종구', '나동빈', '박한울', '이상욱', '이태일']


# count(): 특정한 원소의 개수를 추출
print(my_list.count('이태일'))  # 2


# del: 리스트의 특정 원소를 제거
my_list = ['123', '456', '789']
del my_list[1]
print(my_list)  # ['123', '789']
del my_list[:1]
print(my_list)  # ['789']


# insert(): 리스트에 특정 원소를 삽입
my_list = ['123', '456', '789']
my_list.insert(3, '-1')
print(my_list)  # ['123', '456', '789', '-1']


# append(): 리스트 가장 뒤쪽에 원소를 삽입
my_list = ['123', '456', '789']
my_list.append('-1')
print(my_list)  # ['123', '456', '789', '-1']