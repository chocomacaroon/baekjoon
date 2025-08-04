#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for(char c : s){
        if(isalpha(c)){
            if(isupper(c) && (c+n) > 'Z')
                answer += (c+n-26);
            else if(islower(c) && (c+n) > 'z')
                answer += (c+n-26);
            else
                answer += (c+n);
        }
        else answer += ' ';
    }
    return answer;
}