#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> waiting;
    int days = 0;
    int ans = 1;
    
    days += (100 - progresses[0]) / speeds[0];
    if((100 - progresses[0]) % speeds[0] > 0){
        days+=1;
    }
    
    for(int i = 1; i < progresses.size(); i++){
        progresses[i] += (days*speeds[i]);
        if(progresses[i] >= 100){
            ans += 1;
        }
        else{
            answer.push_back(ans);
            ans = 1;
            days += (100 - progresses[i]) / speeds[i];
            if((100 - progresses[i]) % speeds[i] > 0){
                days+=1;
            }
        }
    }
    answer.push_back(ans);
    return answer;
}

// 93
// 30
// 55

// 100 - 93