#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int j = 0;
    for(int i = 0; i < s.size(); i++){
        j+=1;
        if(s[i] == ' '){
            j=0; 
        }
        if(j%2) answer += toupper(s[i]);
        else answer += tolower(s[i]);
        
    }
    return answer;
}