#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    vector<int> v = tangerine;
    vector<int> cnt;
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    for(int n:v){
        cnt.push_back(count(tangerine.begin(), tangerine.end(), n));
    }
    sort(cnt.begin(), cnt.end(), greater<int>());
    int sum = 0;
    for(int i=0;i<cnt.size();i++){
        sum += cnt[i];
        if(sum >= k){
            return i + 1;
        }
    }
    return answer;
}