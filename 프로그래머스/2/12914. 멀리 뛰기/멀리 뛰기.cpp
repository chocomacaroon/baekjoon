#include <string>
#include <vector>

using namespace std;

long long solution(int n) {
    if(n == 0 || n == 1) return 1;

    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    dp[1] = 1;

    for(int i = 2; i <= n; ++i){
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
    }

    return dp[n];
}
