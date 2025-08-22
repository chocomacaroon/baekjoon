#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> res;
    vector<int> residue;
    int days = 0;
    int cnt = 0;
    for (int i = 0; i < progresses.size(); i++){
        residue.push_back(100 - progresses[i]);
    }
    for (int i = 0; i < progresses.size(); i++){
        residue[i] -= (speeds[i]*days);
        if(residue[i] > 0){
            if(cnt > 0)
                answer.push_back(cnt);
            cnt = 1;
            days += residue[i] / speeds[i];
            if (residue[i] % speeds[i]) days += 1;
        }
        else{
            cnt+=1;
        }
        res.push_back(days);
    }
    answer.push_back(cnt);
    return answer;
}    