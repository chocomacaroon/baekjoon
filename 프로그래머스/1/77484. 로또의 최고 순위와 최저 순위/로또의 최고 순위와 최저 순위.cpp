#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> rank = {6, 6, 5, 4, 3, 2, 1};
    vector<int> answer;
    int plus = count(lottos.begin(), lottos.end(), 0);
    int same = 0;
    for(int i = 0; i < win_nums.size(); i++){
        if(find(lottos.begin(), lottos.end(), win_nums[i])!=lottos.end()){
            same += 1;
        }
    }
    
    answer = {rank[plus + same], rank[same]};
    return answer;
}
