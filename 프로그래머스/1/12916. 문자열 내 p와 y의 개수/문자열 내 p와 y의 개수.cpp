#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    int pcnt = 0;
    int ycnt = 0;
    if(count(s.begin(), s.end(),'p') != string::npos){
        pcnt += count(s.begin(), s.end(),'p');
    }
    if(count(s.begin(), s.end(),'P') != string::npos){
        pcnt += count(s.begin(), s.end(),'P');
    }
    if(count(s.begin(), s.end(),'y') != string::npos){
        ycnt += count(s.begin(), s.end(),'y');
    }
    if(count(s.begin(), s.end(),'Y') != string::npos){
        ycnt += count(s.begin(), s.end(),'Y');
    }
    if(pcnt==ycnt){
        return true;
    }
    return false;
}