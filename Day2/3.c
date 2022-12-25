/*
문제 설명

첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1,
두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때
분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.


제한사항
0 <denum1, num1, denum2, num2 < 1,000

입출력 예
denum1	num1	denum2	num2	result
1	    2	    3	    4	    [5, 4]
9	    2	    1	    3	    [29, 6]

입출력 예 설명

입출력 예 #1
1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.

입출력 예 #2
9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.

*/


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int denum1, int num1, int denum2, int num2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(1);
    int a = denum1 * num2 + denum2 * num1;
    int b = num1 * num2;
    int c = 1;

for(int i = 1; i <= a; i++){
	if(a % i == 0 && b % i == 0){
		c = i;
	}
}
answer[0] = a/c;
answer[1] = b/c;

    return answer;
}