#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    vector<int> v;
    for(int i = 0; i < score.size(); i++){
        v.push_back(score[i]);
        sort(v.begin(), v.end(), greater<int>{});
        if(v.size() >= k)
            answer.push_back(v[k-1]);
        else
            answer.push_back(v[v.size()-1]);
    }
    
    return answer;
}