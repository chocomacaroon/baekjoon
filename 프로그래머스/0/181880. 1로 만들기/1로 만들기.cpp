#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    for(auto n:num_list){
        while(1){
            if(n==1){
                break;
            }
            answer++;
            if(n%2==0){
                n/=2;
            }
            else{
                n = (n-1)/2;
            }
        }
    }
    return answer;
}