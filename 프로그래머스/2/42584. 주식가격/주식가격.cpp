#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size());
    vector<int> stk;
    
    for(int i = 0; i < prices.size(); i++){
        while(!stk.empty() && prices[stk.back()] > prices[i]){
            int p = stk.back();
            stk.pop_back();
            answer[p] = i - p;
        }
        stk.push_back(i);
    }
    while(!stk.empty()){
        int p = stk.back();
        stk.pop_back();
        answer[p] = (prices.size()-1)-p;
    }
    return answer;
}

// 1 2 3 