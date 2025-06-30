#include <string>
#include <vector>
#include <cmath>

using namespace std;

int cnt(int n){
    int res = 0;
    for(int i = 1; i < int(sqrt(n))+1; i++){
        if(n % i == 0)
            res += 2;
    }
    if(n == int(sqrt(n))*int(sqrt(n))){
        res  -= 1;
    }
    return res;
}
int solution(int number, int limit, int power) {
    int answer = 0;
    for(int i = 1; i <= number; i++){
        if(cnt(i) <= limit){
            answer += cnt(i);
        }
        else{
            answer += power;
        }  
    }
    return answer;
}