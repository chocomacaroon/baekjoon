#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    int score;
    for(int i = 0; i < photo.size(); i++){
        score = 0;
        for(string s:photo[i]){
            if(find(name.begin(), name.end(), s) != name.end())
                score += yearning[find(name.begin(), name.end(), s) - name.begin()];
        }
        answer.push_back(score);
    }
    
    return answer;
}