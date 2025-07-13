#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

string solution(string new_id) {
    string answer = "";
    for(char c:new_id){
        if(isupper(c))
            answer += tolower(c);
        else if(islower(c) || isdigit(c) || c == '-' || c == '_' || c == '.'){
            answer += c;
        }
    }
    while(answer.find("..") != string::npos)
        answer.replace(answer.find(".."), 2, ".");
    if(answer[0] == '.'){
        answer.erase(0, 1);
    }
    if(answer[answer.size()-1] == '.'){
        answer.erase(answer.size()-1, 1);
    }
    if(answer.empty())
        answer += 'a';
    if(answer.size() >= 16){
        answer.erase(15,answer.size()-15);
    }
    if(answer[answer.size()-1] == '.'){
        answer.erase(answer.size()-1, 1);
    }
    while(answer.size() <= 2){
        answer += answer[answer.size()-1];
    }
    return answer;
}