#include <string>
#include <vector>
#include <numeric>

using namespace std;

string solution(string s) {
    string answer = "";
    bool flag = true;
    for(char c:s){
        if(flag){
            if(isalpha(c) && islower(c))
                answer += toupper(c);
            else
                answer += c;
            flag = false;
        }
        else{
            if(isupper(c))
                answer += tolower(c);
            else
                answer += c;
        }
        if(c == ' '){
                flag = true;
            }
    }
    return answer;
}