#include <string>
#include <vector>
#include <cmath>

using namespace std;

int count(int n){
    int res = 0;
    for(int i = 1; i < int(sqrt(n))+1; i++){
        if(n%i==0) res += 2;
    }
    if (n == int(sqrt(n))*int(sqrt(n))) res-=1;
    return res;
}

int solution(int left, int right) {
    int answer = 0;
    for(int i = left; i <= right; i++){
        if(count(i)%2) answer -= i;
        else answer += i;
    }
    return answer;
}