#include <string>
#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    
    unordered_map<int, int> left, right;
    for(int n : topping) right[n]+=1;
    int lType = 0; 
    int rType = right.size();
    for(int i = 0; i < topping.size()-1; i++){
        left[topping[i]] += 1;
        right[topping[i]] -= 1;
        if(left[topping[i]] == 1) lType+=1;
        if(right[topping[i]] == 0) rType-=1;
        if(lType == rType) answer+=1;
    }
    return answer;
}

// 