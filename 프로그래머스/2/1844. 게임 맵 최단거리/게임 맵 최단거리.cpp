#include<vector>
#include <queue>
using namespace std;

int solution(vector<vector<int> > maps)
{   
    vector<int> dx = {0,0,1,-1};
    vector<int> dy = {1,-1,0,0};
    
    queue<pair<int,int>> q;
    q.push({0,0});
    
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < maps.size() && 0 <= ny && ny < maps[0].size() && maps[nx][ny] == 1){
                maps[nx][ny] = maps[x][y] + 1;
                q.push({nx,ny});
            }
        }
    }
    if(maps[maps.size()-1][maps[0].size()-1] == 1) return -1;
    return maps[maps.size()-1][maps[0].size()-1];
}