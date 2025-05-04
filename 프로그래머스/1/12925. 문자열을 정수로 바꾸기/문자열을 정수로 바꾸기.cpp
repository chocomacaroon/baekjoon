#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    if(s[0]=='-'){
        return -stoi(s.substr(1, s.length()-1));
    }
    return stoi(s);
}