# 튜플(Tuple): 리스트(List)와 비슷한 자료형 (변경 불가)
tuple = (1, 2, 3)
for i in tuple:
	print(i)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
print(tuple)  # ([1, 2, 3], [4, 5, 6])
print(tuple[0][1])  # 2

# tuple[0] = [7, 8, 9]  # TypeError: 'tuple' object does not support item assignment
tuple[0][1] = 7
print(tuple[0][1])  # 7
"""
	튜플의 값은 변경 불가능하지만, 요소인 리스트의 값은 변경할 수 있다.
"""
# 인덱싱, 슬라이싱 등의 문법도 그대로 사용이 가능
tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple[0:5])  # (1, 2, 3, 4, 5)
print(tuple[0:5] * 3)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

