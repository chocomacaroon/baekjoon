#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool flag = true;
    for (char c:s){
        if (c == ' '){
            flag = true;
            answer += c;
        }
        else{
            if (flag == true){
                flag = false;
                answer += toupper(c);
            }
            else{
                answer += tolower(c);
            }
        }
    }
    return answer;
}