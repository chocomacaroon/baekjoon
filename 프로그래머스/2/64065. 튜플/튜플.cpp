#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<vector<int>> vs;
    s = s.substr(1, s.size()-2);
    string num;
    vector<int> tmp;
    for(char c:s){
        if(c == '{'){
            tmp.clear();
        }
        else if(c == '}'){
            tmp.push_back(stoi(num));
            vs.push_back(tmp);
        }
        else if(num != "" && c == ','){
            tmp.push_back(stoi(num));
            num = "";
        }
        else{
            num += c;
        }
    }
    sort(vs.begin(), vs.end(), [](vector<int> v1, vector<int> v2){return v1.size() <= v2.size();});
    for(auto a:vs){
        for(auto n : a)
            if ( find(answer.begin(), answer.end(), n) == answer.end()){
                answer.push_back(n);
            }
    }
    return answer;
}