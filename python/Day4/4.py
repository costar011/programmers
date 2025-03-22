# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
# 1 ≤ my_string의 길이 ≤ 1,000

# my_string	return
#"jaron"	"noraj"
#"bread"	"daerb"

def solution(my_string):
    return my_string[::-1]

# my_string[::-1]가 문자열을 뒤집는 이유는 Python의 슬라이싱(slicing) 기능 때문
# Python에서는 리스트나 문자열과 같은 시퀀스 데이터 타입에서 슬라이싱을 사용하여 특정 범위의 요소를 선택할 수 있음
# 슬라이싱의 기본 구문은 sequence[start:stop:step]