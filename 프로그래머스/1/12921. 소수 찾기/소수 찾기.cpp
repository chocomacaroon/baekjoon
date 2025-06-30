#include <string>
#include <vector>
#include <numeric>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<bool> v(n+1,true);
    v[0] = false;
    v[1] = false;
    for(int i = 2; i < int(sqrt(n))+1; i++){
        for(int j = i*2; j <= n; j+=i){
            v[j] = false;
        }
    }
    answer = accumulate(v.begin(), v.end(), 0);
    return answer;
}