#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    string s_a = "";
    while(n>0){
        s_a += to_string(n%3);
        n /= 3;
    }
    reverse(s_a.begin(), s_a.end());
    for(int i = 0; i < s_a.size(); i++){
        answer += ((s_a[i]-'0'))*(pow(3,i));
    }
    return answer;
}