#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string s)
{
    vector<char> v;
    for(char c:s){
        if(v.empty()){
            v.push_back(c);
        }
        else{
            if(v.back() == c)
                v.pop_back();
            else
                v.push_back(c);
        }
    }
    if(v.empty()) return 1;
    else return 0;
}