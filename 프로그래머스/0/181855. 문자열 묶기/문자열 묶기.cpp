#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<string> strArr) {
    int answer = 0;
    map <int, int> m;
    for(auto s:strArr){
        m[s.size()] += 1;
    }
    for(auto n:m){
        answer = max(answer, n.second);
    }
    return answer;
}