#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> ans;

void dfs(vector<bool> visited, string now, string target, vector<string> words, int cnt){
    if(now == target){
        ans.push_back(cnt);
        return;
    }
    for(int i = 0; i < words.size(); i++){
        int cnt_now = 0;
        int cnt_tar = 0;
        if(!visited[i]){
            for(int j = 0; j < words[i].size(); j++)
                if(words[i][j] != now[j]) cnt_now+=1;
            if(cnt_now == 1){
                visited[i] = true;
                dfs(visited, words[i], target, words, cnt+1);
            }
        }
    }
    return ;
}

int solution(string begin, string target, vector<string> words) {
    vector<bool> visited(words.size(),false);
    dfs(visited, begin, target, words, 0);
    if(ans.empty()) return 0;
    return *min_element(ans.begin(), ans.end());
}

//hit -> hot -> dot -> 
//두글자가 같고 하나가 target이랑 같은 문자가 있는가?
//그 글자로
//

//한문자만 바꾸는데 target과 겹치게 바꾸는 방법