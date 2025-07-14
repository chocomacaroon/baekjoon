#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    unordered_map<string, int> m;
    
    for(int i = 0; i < players.size(); i++){
        m[players[i]] = i;
    }
    
    for(int i = 0; i < callings.size(); i++){
        int idx1 = m[callings[i]];
        int idx2 = idx1 - 1;
        
        string ply1 = players[idx1];
        string ply2 = players[idx2];
        
        swap(players[idx1], players[idx2]);
        
        m[ply1] = idx2;
        m[ply2] = idx1;
    }
    return players;
}