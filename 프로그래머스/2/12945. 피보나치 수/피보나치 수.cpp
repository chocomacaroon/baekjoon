#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    vector<int> v = {0, 1};
    int answer = 0;
    if(n == 0 || n == 1) return n;
    for(int i = 2; i <= n; i++){
        v.push_back((v[i-1]+v[i-2])%1234567);
    }
    return v.back()%1234567;
}