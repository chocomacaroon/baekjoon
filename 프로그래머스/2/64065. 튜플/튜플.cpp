#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int i = 1;
    vector<vector<int>> v;
    while(i < s.size()-1){
        string n;
        vector<int> tmp;
        if(s[i] == '{'){
            n = "";
            i+=1;
            while(s[i]!='}'){
                if(isdigit(s[i])){
                    n += s[i];
                }
                else{
                    tmp.push_back(stoi(n));
                    n = "";
                }
                i+=1;
            }
            if(n!=""){
                tmp.push_back(stoi(n));
            }   
        }
        if(!tmp.empty()){
            v.push_back(tmp);
            tmp = {};
        }
        i+=1;
    }
    
    sort(v.begin(), v.end(),[](const vector<int>& a, const vector<int>& b) {return a.size() < b.size();});
    int sum = 0;
    if(v.size()>0){
        answer.push_back(v[0][0]);
        sum += v[0][0];
    }
    for(int i = 1; i < v.size(); i++){
        answer.push_back(accumulate(v[i].begin(), v[i].end(),0)-sum);
        sum = accumulate(v[i].begin(), v[i].end(),0);
    }
    return answer;
}