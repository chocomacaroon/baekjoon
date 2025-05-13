#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    for(auto p:photo){
        int res = 0;
        for(auto n:p){
            if(find(name.begin(), name.end(), n) != name.end()){
                res += yearning[distance(name.begin(), find(name.begin(), name.end(), n))];
            }
        }
        answer.push_back(res);
    }
    return answer;
}