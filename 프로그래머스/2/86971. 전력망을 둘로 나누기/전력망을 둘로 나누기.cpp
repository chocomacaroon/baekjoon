#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int dfs(int pos, vector<vector<int>>& graph,  vector <bool> visited){
    
    int count = 1;
    visited[pos] = true;
    for(int i = 0; i < graph[pos].size(); i++)
        if(!visited[graph[pos][i]])
            count += dfs(graph[pos][i], graph, visited);
    return count;
}

int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    for(int i = 0; i < wires.size(); i++){
        vector<vector<int>> graph(n+1);
        for(int j = 0; j < wires.size();j++){
            if(i==j) continue;
            else{
                int a = wires[j][0];
                int b = wires[j][1];
                graph[a].push_back(b);
                graph[b].push_back(a);
            }
        }
        int start1 = wires[i][0];
        int start2 = wires[i][1];
        vector <bool> visited(n+1, false);
        int count = dfs(start1, graph, visited); //start1에서 엮여있는 노드수
        answer = min(abs(n - count - count), answer);
    }
    return answer;
}

//모든 간선을 하나씩 끊어보기