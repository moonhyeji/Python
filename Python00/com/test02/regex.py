#reg regular expression 정규표현식
import re             #re라는 모듈,라이브러리를 사용하겠다 하는 것.
from nis import match


'''
Regular Expression
. : 문자 한개
^ : 문자열의 시작 
$ : 문자열의 마지막 
[]: 문자집합 
| : or
(): 괄호 안의 정규식 그룹 

*:    0 or more
+:    1 or more
?:    0 or 1
{n}:  n번 반복 
{n,m}: n번부터 m
{n, }: n번부터 무한번
'''

"""
**** r: 문자열 표기법 (re 모듈의 확장 문법)
\w: [a-zA-Z0-9_]:a~z, A~Z, 0~9, _를 포함하는 모든 문자
\W: [^a-zA-Z0-9_] :위의 문자들을 제외한 나머지 
\d: [0-9]: 0부터 9 
\D: [^0-9]:숫자를 제외한 나머지 
\s: [\t\n\r\f\v] :공백문자
\S: [^\t\n\r\f\v] : 공백문자 제외한 나머지
\b: 단어의 시작과 끝의 빈 공백 
\B: 단어의 시작과 끝이 아닌 빈 공백 
\\: \
\[숫자]: 지정된 숫자만큼 일치하는 문자열 
\A: 문자열의 시작 
\Z: 문자열의 끝 
"""

str01 = '나의 이메일은 ans0127@naver.com 입니다'
match = re.search(r'[\w]*@[a-zA-Z.]*', str01)
print(match.group())

str02 = re.search(r'[\w.-]+@[\w.-]+', str01)
print(str02.group())











