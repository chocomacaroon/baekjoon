#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    vector<int> tmp;
    vector<int> res;
    int pos = 0;
    for(int i = 1; i < order.size()+1; i++){
        while (!tmp.empty() && tmp.back() == order[pos]){
                tmp.pop_back();
                pos+=1;
            }
        if (order[pos] < i)
            tmp.push_back(i);
        else if (order[pos] > i){
            tmp.push_back(i);
            
        }
        else if (order[pos] == i){
            res.push_back(i);
            pos+=1;
        }
    }
    while (!tmp.empty() && tmp.back() == order[pos]){
        tmp.pop_back();
        pos+=1;
    }
    return pos;
}

// 1