#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    vector<string> v;
    
    if(cacheSize == 0){
        return cities.size() * 5;
    }
    
    for(auto city : cities){
        transform(city.begin(), city.end(), city.begin(), 
                  [](unsigned char c){ return tolower(c); });
        auto it = find(v.begin(), v.end(), city);
        if(it != v.end()){ 
            answer += 1;
            v.erase(it);
            v.push_back(city);
        } 
        else{
            answer += 5;
            if (v.size() >= cacheSize) 
                v.erase(v.begin());
            v.push_back(city);
        }
        
    }
    return answer;
}