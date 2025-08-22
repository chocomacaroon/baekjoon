#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int dfs(vector<bool> visited, int k, vector<vector<int>> dungeons){
    int max_dungeons_count = 0;
    
    for (int i = 0; i < visited.size(); i++){
        if (!visited[i] && k >= dungeons[i][0]){
            visited[i] = true;
            int current_dungeons = 1 + dfs(visited, k - dungeons[i][1], dungeons);
            max_dungeons_count = max(max_dungeons_count, current_dungeons);
            visited[i] = false;
        }
    }
    return max_dungeons_count;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = 0;
    vector<bool> visited(dungeons.size(), false);
    return dfs(visited, k, dungeons);
    return answer;
}

// n와 m 문제 처럼 모든 경우를 다 가보기
// 80
// 80 20
// 50 40
// 30 10