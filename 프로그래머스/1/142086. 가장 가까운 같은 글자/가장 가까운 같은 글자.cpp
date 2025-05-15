#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<char> tmp;
    vector<char> rev;
    for(int i = 0; i < s.size(); i++){
        rev = tmp;
        reverse(rev.begin(), rev.end());
        if(find(tmp.begin(), tmp.end(), s[i]) == tmp.end()){
            answer.push_back(-1);
        }
        else{
            answer.push_back(find(rev.begin(), rev.end(), s[i]) - rev.begin()+1);
        }
        tmp.push_back(s[i]);
    }
    return answer;
}