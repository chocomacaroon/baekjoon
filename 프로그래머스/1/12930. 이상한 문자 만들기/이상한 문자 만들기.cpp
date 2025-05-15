#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int pos = 1;
    for(int i = 0; i < s.size(); i++){
        if(isalpha(s[i])){
            if(pos%2==0)
                answer += tolower(s[i]);
            else
                answer += toupper(s[i]);
            pos+=1;
        }
        else{
            answer += s[i];
            pos = 1;
        }
    }
    return answer;
}