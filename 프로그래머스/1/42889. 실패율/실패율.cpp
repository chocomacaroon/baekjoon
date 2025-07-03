#include <string>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<double> rate;
    int sum = 0;
    int num = 0;
    for(int i = 0; i < N; i++){
        num = count(stages.begin(), stages.end(), i+1);
        if(stages.size()==sum)
            rate.push_back(0);
        else
            rate.push_back((double)num/(stages.size()-sum));
        sum += num;
    }
    vector<int> idx;
    for(int i = 0; i < N; i++){
        idx.push_back(i+1);
    }
    sort(idx.begin(), idx.end(), [&rate](int a, int b){
        if(rate[a-1] == rate[b-1]) return a < b;
        return rate[a-1] > rate[b-1];
    });
    return idx;
}