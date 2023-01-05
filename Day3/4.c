/*
문제 설명

정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴
배열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 100

입출력 예
n	    result
10	    [1, 3, 5, 7, 9]
15	    [1, 3, 5, 7, 9, 11, 13, 15]

입출력 예 설명

입출력 #1
10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.

입출력 #1
15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.

*/

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int a = 0, i;
    int* answer = (int*)malloc(((n/2)+1) * sizeof(int));
    
    for(i = 1; i <= n; i = i+2) {
        answer[a] = i;
        a++;
    }
    
    
    return answer;
}