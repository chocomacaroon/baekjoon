#include <string>
#include <vector>

using namespace std;

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = 0;
    
    for(int i = 0; i < schedules.size(); i++){
        bool ok = true;
        int day = startday;
        int deadline = schedules[i]/100*60 + schedules[i]%100 +10;
        for(int j = 0; j < timelogs[i].size(); j++){
            int total = timelogs[i][j]/100*60 + timelogs[i][j]%100;
            if(day%7 != 0 && day%7 != 6){ 
                if(total > deadline){
                    ok = false;
                    break;
                }
            }
            day+=1; 
        }
        if(ok) answer+=1;
    }
    return answer;
}