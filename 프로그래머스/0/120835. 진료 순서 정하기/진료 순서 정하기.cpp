#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    vector<int> sorted = emergency;
    sort(sorted.begin(), sorted.end(), greater<int>{});
    for(auto n : emergency){
        answer.push_back(find(sorted.begin(), sorted.end(), n)-sorted.begin()+1);
    }
    return answer;
}