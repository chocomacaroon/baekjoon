#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    vector<string> cache;
    for(auto s:cities){
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        auto it = find(cache.begin(), cache.end(), s);
        if(it != cache.end()){
            answer += 1;
            cache.erase(it);
        }
        else{
            answer += 5;
            if(cache.size() == cacheSize && cacheSize > 0){
                cache.erase(cache.begin());
            }
        }
        if(cacheSize>0)
            cache.push_back(s);
    }
    return answer;
}