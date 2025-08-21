#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    vector<string> before;
    
    before.push_back(words[0]);
    
    for(int i = 1; i < words.size(); i++){
        if (find(before.begin(), before.end(), words[i]) == before.end() && before.back().back() == words[i][0]){
            before.push_back(words[i]);
        }
        else{
            return {i%n+1, i/n+1};
        }
    }
    return {0,0};
}