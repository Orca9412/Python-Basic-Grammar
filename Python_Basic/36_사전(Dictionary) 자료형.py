# 사전(Dictionary): 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'
print(dict)  # {'안녕': 'Hello', '기적': 'Miracle', '노력': 'effort'}


for i, k in enumerate(dict):
	print(f"[인덱스: {i}] 한글: {k} / 영어: {dict[k]}")


dict['안녕'] = 'Hi'  # 특정한 키 인덱스로 접근해서, 값을 바꿀 수 있다.
print(dict)  # {'안녕': 'Hi', '기적': 'Miracle', '노력': 'effort'}


# 특정 데이터가 순서와 상관없이 어떤 데이터가 어떤 자료구조에 포함여부를 검증 목적으로 매우 편리
# 값 삭제: del 키워드
del dict['기적']
print(dict)  # {'안녕': 'Hi', '노력': 'effort'}


# 초기화: clear()
dict.clear()
print(dict)  # {}


# 사전 자료형의 길이: len()
print(f"사전 자료형의 길이: {len(dict)}")  # 사전 자료형의 길이: 0

# 키 인덱스만 출력하기: keys()
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'
keys = dict.keys()
key_list = list(keys)  # list 형변환
print(f"키: {key_list}")  # 키: ['안녕', '기적', '노력']


# 값만 출력하기: values()
values = dict.values()
value_list = list(values)
print(f"값: {value_list}")  # 값: ['Hello', 'Miracle', 'effort']


# 특정 키 존재 여부 확인 => 리스트, 튜플 등과 동일하게 사용됨
if '노력' in dict:
	print("[노력] 키가 존재합니다.")


# 정렬
scores = {}
scores['나동빈'] = 78
scores['이태일'] = 99
scores['박한울'] = 85
# 키로 정렬하기: sorted()
print(sorted(scores))  # ['나동빈', '박한울', '이태일']
# 내림차순 정렬: sorted(reverse=True)
print(sorted(scores, reverse=True))  # ['이태일', '박한울', '나동빈']

# 값 정렬하기
print(sorted(scores.values()))  # [78, 85, 99]

