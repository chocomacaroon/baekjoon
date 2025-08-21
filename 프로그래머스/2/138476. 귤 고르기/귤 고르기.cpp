#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    map<int, int> m;
    for (int t:tangerine){
        m[t]+=1;
    }
    vector<pair<int, int>> v;
    for(auto const& pair: m){
        v.push_back({pair.first, pair.second});
    }
    sort(v.begin(), v.end(), [](const pair<int, int>& a, const pair<int, int>& b){return a.second > b.second;});
    int total = 0;
    for (auto const& pair:v){
        total += pair.second;
        answer+=1;
        if(total >= k){
            break;
        }
    }
    return answer;
}