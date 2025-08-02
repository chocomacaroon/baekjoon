#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(int a, int b, int c, int d) {
    int answer = 1;
    vector<int> dice = {a,b,c,d};
    map <int, int> m;
    for(int num : dice) m[num]+=1;

    if(m.size()==1){
        int p = dice[0];
        return 1111*p;
    }
    else if(m.size()==2){
        vector<int> keys;
        for(auto& kv : m){
            keys.push_back(kv.first);
        }
        int count1 = m[keys[0]];
        int count2 = m[keys[1]];
        
        if(count1 == 3 || count2 == 3){
            int p = (count1 == 3) ? keys[0] : keys[1];
            int q = (count1 == 3) ? keys[1] : keys[0];
            int val = 10 * p + q;
            return val * val;
        }
        else{
            int p = keys[0];
            int q = keys[1];
            return (p+q)*abs(p-q);
        }
    }
    else if(m.size() == 3){
        int p = -1;
        int q = -1;
        int r = -1;
        for(auto& kv : m){
            if(kv.second == 2) p = kv.first;
        }
        vector<int> others;
        for(auto& kv : m){
            if(kv.second == 1) others.push_back(kv.first);
        }
            q = others[0];
            r = others[1];
            return q * r;
    }
    else{
        return *min_element(dice.begin(), dice.end());
    }
    return answer;
}