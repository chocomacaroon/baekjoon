#include <string>
#include <vector>

using namespace std;

void dfs(int pos, int n, vector<bool>& visited, vector<vector<int>> computers){
    visited[pos] = true;
    for(int i = 0; i < n; i++){
        if(computers[pos][i] == 1 && i!=pos && !visited[i]){
            dfs(i, n, visited, computers);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n,false);
    for(int i = 0; i < n; i++){
        if(!visited[i]){
            dfs(i,n,visited,computers);
            answer+=1;
        }
    }
    return answer;
}

//그래프 그룹 몇개 있는지 체크하는 문제