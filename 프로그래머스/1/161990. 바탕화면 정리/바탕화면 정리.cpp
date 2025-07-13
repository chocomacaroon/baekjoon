#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    vector<int> answer;
    vector<int> x;
    vector<int> y;
    for(int i = 0; i < wallpaper.size(); i++)
        for(int j = 0; j < wallpaper[0].size(); j++){
            if(wallpaper[i][j] == '#'){
                x.push_back(i);
                y.push_back(j);
            }
        }
    answer = {*min_element(x.begin(), x.end()), *min_element(y.begin(), y.end()), *max_element(x.begin(), x.end())+1, *max_element(y.begin(), y.end())+1};
    return answer;
}

// 왼 오 위 아래