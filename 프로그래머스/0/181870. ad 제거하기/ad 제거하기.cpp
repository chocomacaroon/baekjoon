#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    for(auto s:strArr){
        if(s.find("ad") == string::npos){
            answer.push_back(s);
        }
    }
    return answer;
}