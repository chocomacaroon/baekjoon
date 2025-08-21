#include <iostream>
#include<string>
#include <vector>

using namespace std;

int solution(string s)
{
    int answer = -1;
    vector<char> stk;
    for(char c:s){
        if (!stk.empty()){
            if(stk.back()==c){
                stk.pop_back();
            }
            else{
                stk.push_back(c);
            }
        }
        else{
            stk.push_back(c);
        }
    }
    if(stk.empty()) return 1;
    return 0;
    return answer;
}