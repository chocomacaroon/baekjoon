#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> ans;

void dfs(int k, vector<vector<int>> dungeons, int cnt, vector<bool> v){
    ans.push_back(cnt);
    for(int i = 0; i < dungeons.size(); i++){
        if(!v[i] && k >= dungeons[i][0]){
            v[i] = true;
            dfs(k - dungeons[i][1],dungeons, cnt+1, v);
            v[i] = false;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    ans.clear();
    queue<int> q;
    vector<bool> v(dungeons.size(), false);
    dfs(k, dungeons, 0, v);
    answer = *max_element(ans.begin(), ans.end());
    return answer;
}
