#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int p = 0;
    int y = 0;
    for(char c:s){
        if(c == 'p' || c == 'P'){
            p += 1;
        }
        if(c == 'y' || c == 'Y'){
            y += 1;
        }
    }
    return (p==y)?true:false;
}