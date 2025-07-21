#include<vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    queue<vector<int>> q;
    
    
    vector<int> dx = {1, -1, 0, 0};
    vector<int> dy = {0, 0, 1, -1};
    vector<int> ans;
    vector<vector<bool>> v(maps.size(), vector<bool>(maps[0].size(), false)); // 몇 곱하기 몇 벡터인지
    
    q.push({0,0});
    v[0][0] = true;
    
    //visit 조건 있어야됨
    while(!q.empty()){
        
        int x = q.front()[0];
        int y = q.front()[1];
        
        q.pop();
        
        if(x == maps.size()-1 && y == maps[0].size()-1){
            ans.push_back(maps[x][y]);
        }
        for(int i = 0; i < 4; i++){
            if(x+dx[i] >= 0 && x+dx[i] < maps.size() && y+dy[i] >= 0 && y+dy[i] < maps[0].size()){
                if(maps[x+dx[i]][y+dy[i]] != 0 && v[x+dx[i]][y+dy[i]] == false){
                    maps[x+dx[i]][y+dy[i]] += maps[x][y];
                    q.push({x+dx[i], y+dy[i]});
                    v[x+dx[i]][y+dy[i]] = true;
                }
            }
        }
    }
    if(!ans.empty()) return *min_element(ans.begin(), ans.end());
    else return -1;
}