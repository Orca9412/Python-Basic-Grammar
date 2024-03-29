"""
	리스트 자료형의 기본 함수
"""
a = [10, 20, 30, 40, 50, 10, 10]
print(a)

# 1. count(원소) 함수: 리스트 내 특정 원소가 몇 개 포함되어 있는지 반환
print(a.count(10))  # 3

# 2. index(원소) 함수: 리스트 내 특정 원소의 인덱스 반환
print(a.index(50))  # 4

# 3. append(원소) 함수: 리스트 뒤쪽에 새로운 원소 삽입
a.append(25)
print(a)  # [10, 20, 30, 40, 50, 10, 10, 25]

# 4. sort() 함수: 리스트를 오름차순으로 정렬
a.sort()  # 기본값인 오름차순 정렬
print(a)  # [10, 10, 10, 20, 25, 30, 40, 50]

# 5. extend(리스트) 함수: 리스트의 뒤쪽에 다른 리스트를 삽입(확장)
b = [70, 50, 40]
a.extend(b)
print(a)  # [10, 10, 10, 20, 25, 30, 40, 50, 70, 50, 40]

# 6. insert(인덱스, 원소) 함수: 특정한 인덱스 위치에 특정한 원소를 삽입
a.insert(3, 70)
print(a)  # [10, 10, 10, 70, 20, 25, 30, 40, 50, 70, 50, 40]

# 7. remove(원소): 리스트 내 특정 원소를 삭제
a = [10, 20, 30, 40, 50, 10, 10]
a.remove(10)
print(a)  # [20, 30, 40, 50, 10, 10]

# 8. pop(원소) 함수: 리스트 내 특정 인덱스의 원소 삭제
a.pop(3)
print(a)  # [20, 30, 40, 10, 10]

# 9. reverse() 함수: 리스트를 뒤집기
a.reverse()
print(a)  # [10, 10, 40, 30, 20]




