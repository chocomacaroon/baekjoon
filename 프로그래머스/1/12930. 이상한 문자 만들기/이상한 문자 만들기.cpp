#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int idx = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i]==' '){
            answer += ' ';
            idx = 0;
        }
        else{
            idx+=1;
            if(idx%2==0){
            answer += tolower(s[i]);
        }
        else if(idx%2!=0){
            answer += toupper(s[i]);
        }
        }
        
    }
    return answer;
}