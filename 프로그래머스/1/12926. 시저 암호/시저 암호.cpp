#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for(int i = 0; i < s.size(); i++){
        char c = s[i];
        if(isalpha(c)){
            for(int j = 0; j < n; j++){
            if(c == 'z'){
                c = 'a';
            }
            else if(c == 'Z'){
                c = 'A';
            }
            else{
                c+=1;
            }
        }
    }
        answer += c;    
    }
    return answer;
}