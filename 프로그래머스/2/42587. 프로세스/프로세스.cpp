#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<int> nums;
    vector<int> v;
    
    for(int i = 0; i < priorities.size(); i++){
        nums.push(i);
    }
    
    while(!nums.empty()){
        int n = nums.front();
        if(priorities[n] < *max_element(priorities.begin(), priorities.end())){
            nums.pop();
            nums.push(n);
        }
        else{
            priorities[n] = 0;
            nums.pop();
            v.push_back(n);
        }
    }
    return find(v.begin(), v.end(), location)-v.begin()+1;
    return answer;
}