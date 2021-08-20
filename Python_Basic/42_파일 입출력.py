# 파일 입출력
# 동일한 위치에 있을 때는 바로 읽을 수 있다.

# open(): 파일을 특정한 모드로 여는 함수
# read(): 파일 객체로부터 모든 내용을 읽는 함수
# 읽기: r, 쓰기: w
f = open('input.txt', 'r', encoding="UTF-8")
data = f.read()
print(data)
f.close()  # 해당 파일에 대한 리소스 사용이 끝남을 정의


# seek(): 특정 위치부터 파일을 읽을 수 있다.
f.seek(9)  # 한글은 3바이트이므로, 9바이트 이후부터 파일을 읽음
data = f.read()
print(data)
f.close()

# readline(): 파일 객체로부터 한 줄씩 문자열을 읽는 함수
count = 0
while count < 3:
	data = f.readline()
	count += 1
	print(f"{count}번째 줄: {data}", end='')  # end='': 줄바꿈 중복 방지
f.close()


# readlines(): 전체 내용을 한 번에 리스트에 담는 함수
list = f.readlines()
for i, data in enumerate(list):
	print(f"{i+1}번째 줄: {data}", end='')
f.close()


# with: 파일 입출력 자동화, 자동으로 할당 해제까지 이루어짐
with open("input.txt", 'r', encoding='UTF-8') as f:
	list = f.readlines()
	for i, data in enumerate(list):
		print(f"{i + 1}번째 줄: {data}", end='')


# 파일에 포함된 문자를 처리하는 방법: 파일에 포함된 문자의 빈도수 체크
def process(filename):
	with open(filename, 'r') as f:
		# 키: 알파벳, 값: 빈도수
		dict = {}
		data = f.read()
		for i in data:
			if i in dict:
				dict[i] += 1
			else:
				dict[i] = 1
	return dict

dict = process('input.txt')
# 빈도수를 기준으로 내림차순 정렬
dict = sorted(dict.items(), key = lambda a: a[1], reverse=True)
for data, count in dict:
	if data == '\n' or data == ' ' or data == '.':
		continue
	print(f"{count}번 출현: [{data}]")