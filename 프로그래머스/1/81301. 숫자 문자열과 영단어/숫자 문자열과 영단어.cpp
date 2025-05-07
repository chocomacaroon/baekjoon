#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

using namespace std;

int solution(string s) {
    int answer = 0;
    string tmp = "";
    vector<string> number{"zero","one","two","three","four","five","six","seven","eight","nine"};
    for(int i = 0; i < s.size(); i++){
        if(isdigit(s[i])){
            answer = answer*10+s[i]-'0';
        }
        else{
            tmp += s[i];
        }
        if(find(number.begin(), number.end(), tmp) != number.end()){
            answer = answer*10+distance(number.begin(), find(number.begin(), number.end(), tmp));
            tmp = "";
        }
    }
    return answer;
}