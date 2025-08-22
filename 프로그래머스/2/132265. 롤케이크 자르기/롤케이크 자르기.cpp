#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    
    map <int, int> right_counts;
    for(int t : topping){
        right_counts[t]++;
    }
    map<int, int> left_counts;
    
    for(int t : topping){
        left_counts[t]++;
        right_counts[t]--;
        if(right_counts[t] == 0){
            right_counts.erase(t);
        }
        if(left_counts.size() == right_counts.size()){
            answer++;
        }
    }
    return answer;
}