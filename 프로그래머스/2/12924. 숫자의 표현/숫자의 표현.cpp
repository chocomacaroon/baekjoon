#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    // for(int i = 1; i <= n; i++){
    //     if(i%2==1){
    //         if((n/i)*i == n){
    //             answer += 1;
    //         }
    //     }
    //     else{
    //         if((n/i*2+1)*(i/2) == n){
    //             answer += 1;
    //         }
    //     }
    // }
    for(int i = 1; i <= n; i++){
        int sum = 0;
        for(int j = i; j <= n; j++){
            sum += j;
            if(sum == n){
                answer+=1;
                break;
            }
            else if(sum > n){
                break;
            }
        }
    }
    return answer;
}