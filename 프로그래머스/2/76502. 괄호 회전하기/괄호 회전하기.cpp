#include <string>
#include <vector>

using namespace std;

bool right(string s){
    vector<char> v;
    for(char c:s){
        if(v.empty()) v.push_back(c);
        else if(c==']' && v.back()=='['){
            v.pop_back();
        }
        else if(c==')' && v.back()=='('){
            v.pop_back();
        }
        else if(c=='}' && v.back()=='{'){
            v.pop_back();
        }
        else{
            v.push_back(c);
        }
    }
    if(v.empty()) return true;
    return false;
}
int solution(string s) {
    int answer = 0;
    for(int i = 0; i < s.size(); i++){
        s = s.substr(1,s.size()-1) + s[0];
        if(right(s))
            answer+=1;
    }
    return answer;
}