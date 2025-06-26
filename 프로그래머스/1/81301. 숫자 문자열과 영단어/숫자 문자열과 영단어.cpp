#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string s) {
    int answer = 0;
    vector<string> d = {"zero", "one","two","three","four", "five","six","seven","eight","nine"};
    string tmp = "";
    for(int i = 0; i < s.size(); i++){
        if(isalpha(s[i])){
            tmp += s[i];
            if(find(d.begin(), d.end(),tmp)!=d.end()){
                answer = answer * 10 + find(d.begin(), d.end(), tmp) - d.begin();
                tmp = "";
            }
        }
        else if(isdigit(s[i])){
            answer = answer * 10 + (s[i]-'0');
        }
    }
    return answer;
}