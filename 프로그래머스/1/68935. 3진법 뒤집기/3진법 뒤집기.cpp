#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int solution(int n) {
    int answer = 0;
    string tmp = "";
    while(n>0){
        tmp += to_string(n%3);
        n /= 3;
    }
    if(n>0) tmp += to_string(n);
    reverse(tmp.begin(), tmp.end());
    for(int i = 0; i < tmp.size(); i++){
        answer += ((tmp[i]-'0')*pow(3,i));
    }
    return answer;
}