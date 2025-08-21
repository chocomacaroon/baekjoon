#include<string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<char> stk;
    for (auto c:s){
        if (c == '('){
            stk.push_back(c);
        }
        else if (c == ')'){
            if (!stk.empty() && stk.back() == '('){
                stk.pop_back();
            }
            else{
                stk.push_back(c);
            }
        }
    }
    if (!stk.empty()){
        return false;
    }
    else{
        return true;
    }
    return answer;
}