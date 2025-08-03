#include <string>
#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    int m = x;
    for(long long i = 0; i < n; i++){
        answer.push_back(m);
        m += x;
    }
    return answer;
}