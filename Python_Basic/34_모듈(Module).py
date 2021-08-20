# 모듈(Module): 미리 작성된 함수 코드를 모아 놓은 파이썬 파일
import math  # math 라이브러리
print(math.pow(3, 8))  # pow: 제곱 기능 제공
print(math.sqrt(64))  # sqrt: 제곱근
print(math.gcd(72, 24))  # gcd: 최대공약수


# 나만의 라이브러리를 직접 import 해서 사용 가능
import lib  # 내가 만든 lib 라이브러리
print(lib.add(3, 7))  # 10
print(lib.subtract(7, 3))  # 4


# 모듈의 크기가 큰 경우, 특정 기능만 사용 가능
from lib import add
print(add(3, 7))  # 10


# 모듈 파일명이 지나치게 긴 경우, 별칭 사용 가능
import lib as t
print(t.add(3, 7))  # 10

