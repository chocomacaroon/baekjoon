#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    string tmp = "";
    for(auto c:s){
        if(tmp.find(c) == string::npos){
            answer.push_back(-1);
        }
        else{
            answer.push_back(tmp.find(c)+1);
        }
        tmp = c + tmp;
    }
    return answer;
}