#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<char> d;
    for(int i = 0; i < s.size(); i++){
        if(find(d.begin(),d.end(),s[i])==d.end()){
            answer.push_back(-1);
        }
        else{
            answer.push_back(1+find(d.begin(),d.end(),s[i])-d.begin());
        }
        reverse(d.begin(), d.end());
        d.push_back(s[i]);
        reverse(d.begin(), d.end());
    }
    return answer;
}