# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ num_list의 길이 ≤ 1,000
# 0 ≤ num_list의 원소 ≤ 1,000

def solution(num_list):
    return list(reversed(num_list))

# solution이라는 함수를 정의하는
# 이 함수는 num_list라는 매개변수를 받아들이고, num_list의 요소들을 역순으로 정렬한 후 리스트로 반환
# reversed() 함수는 파이썬 내장 함수로, 주어진 시퀀스(리스트, 튜플, 문자열 등)의 요소들을 역순으로 반환 reversed() 함수의 반환값은 이터레이터이므로, list() 함수를 사용하여 이터레이터를 리스트로 변환
# 예를 들어, num_list가 [1, 2, 3, 4, 5]라면, reversed(num_list)는 [5, 4, 3, 2, 1]을 반환하고, list(reversed(num_list))는 [5, 4, 3, 2, 1]을 반환