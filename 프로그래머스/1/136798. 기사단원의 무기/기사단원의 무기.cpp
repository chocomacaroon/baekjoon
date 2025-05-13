#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int number, int limit, int power) {
    int answer = 0;
    int num;
    for(int i = 1; i <= number; i++){
        num = 0;
        for(int j = 1; j <= sqrt(i); j++){
            if(i%j==0){
                num+=2;
                if(j==i/j) num--;
            }
        }
            
        if(num > limit)
            answer += power;
        else
            answer += num;
    }
    return answer;
}