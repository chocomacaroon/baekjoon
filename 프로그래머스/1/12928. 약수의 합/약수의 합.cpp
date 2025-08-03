#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    for(int i = 1; i < int(sqrt(n))+1; i++){
        if(n%i==0){
            answer += i;
            answer += (n/i);
        }
    }
    if(n == int(sqrt(n))*int(sqrt(n))){
        answer -= int(sqrt(n));
    }
    return answer;
}