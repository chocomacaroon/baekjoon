#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<char> word;
    for(int i = 0; i < s.size(); i++){
        if(word.empty() or find(word.begin(), word.end(), s[i]) == word.end()){
            answer.push_back(-1);
        }
        else{
            vector<char> rev = word;
            reverse(rev.begin(), rev.end());
            int dis = distance(rev.begin(), find(rev.begin(), rev.end(), s[i]));
            answer.push_back(i-(word.size()-dis)+1);
        }
        word.push_back(s[i]);
    }
    return answer;
}