#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int sub = 1;
    int sum = 0;
    for(int i = 0; i < num_list.size(); i++){
        sub *= num_list[i];
        sum += num_list[i];
    }
    if(sub < sum*sum){
        return 1;
    }
    else if(sub > sum*sum){
        return 0;
    }
    return answer;
}