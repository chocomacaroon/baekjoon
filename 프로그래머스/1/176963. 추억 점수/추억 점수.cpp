#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    for(int i = 0; i < photo.size(); i++){
        int sum = 0;
        for(auto n : photo[i]){
            if(find(name.begin(), name.end(),n)!=name.end())
                sum += yearning[find(name.begin(), name.end(),n)-name.begin()];
        }
        answer.push_back(sum);
    }
    return answer;
}