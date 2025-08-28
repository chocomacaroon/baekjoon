#include <string>
#include <vector>

using namespace std;

int solution(int x, int y, int n) {
    int answer = 0;
    if (x == y) return 0;
    vector<int> dp(y+1, 1e9);
    dp[x] = 0;
    for(int i = x; i <= y; i++){
        if (dp[i] == 1e9){
            continue;
        }
        if (i+n <= y){
            dp[i+n] = min(dp[i+n], dp[i]+1);
        }
        if (i*2 <= y){
            dp[i*2] = min(dp[i*2], dp[i]+1);
        }
        if (i*3 <= y){
            dp[i*3] = min(dp[i*3], dp[i]+1);
        }
    }
    if(dp[y] == 1e9){
        return -1;
    }
    else{
        return dp[y];
    }
    return answer;
}