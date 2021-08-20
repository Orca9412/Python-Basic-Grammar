# 람다(lambda)식: 함수의 형태를 더욱 짧게 쓸 수 있도록 한다.
# lambda 키워드를 사용한다.
add = lambda x, y: x + y
print(add(1, 2))  # 3

# map(): 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와주는 함수
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
my_function = lambda a, b: a + b
result = map(my_function, list1, list2)  # list1 과 list2 에 my_function 함수를 적용해서 돌려준다.
print(result)  # <map object at 0x0000020B8D1E7B50> 가 출력되므로 list() 함수로 형변환
print(list(result))  # [7, 9, 11, 13, 15]

