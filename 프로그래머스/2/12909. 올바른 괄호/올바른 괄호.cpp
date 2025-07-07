#include<string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<char> v;
    for(char c:s){
        if(v.empty())
            v.push_back(c);
        else{
            if(v[v.size()-1]=='(' && c == ')')
                v.pop_back();
            else
                v.push_back(c);
        }
    }
    if(v.empty()){
        answer = true;
    }
    else answer = false;
    return answer;
}