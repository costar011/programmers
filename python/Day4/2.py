# 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < money ≤ 1,000,000
# 입출력 예
# money	 result
# 5,500	 [1, 0]
# 15,000	 [2, 4000]

def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer

# solution이라는 함수를 정의
# 이 함수는 money라는 매개변수를 받아들이고, answer라는 빈 리스트를 생성
# 그런 다음, answer 리스트에 money를 5500으로 나눈 몫을 추가하고, money를 5500으로 나눈 나머지를 추가
# 마지막으로, answer 리스트를 반환

# append -  파이썬 리스트에 새로운 요소를 추가하는 메서드