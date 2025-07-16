#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(vector<int> elements) {
    int answer = 0;
    set<int> s;
    for(int i = 1; i <= elements.size(); i++){ //i개의 합
        int sum = 0;
        for(int j = 0; j < elements.size(); j++){
            
            if(j+i >= elements.size()){
                sum = accumulate(elements.begin()+j, elements.end(), 0);
                sum += accumulate(elements.begin(), elements.begin()+(j+i-elements.size()),0);
            }
            else{
                sum = accumulate(elements.begin()+j, elements.begin()+(j+i), 0);
            }
            s.insert(sum);
        }
    }
    return s.size();
}

// 7 9 1 1 4
// 16 10 2 5 11
//