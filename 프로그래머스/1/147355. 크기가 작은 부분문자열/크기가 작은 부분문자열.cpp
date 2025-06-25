#include <string>
#include <vector>
#include <iostream> 

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    vector<int> v;
    for(int i = 0; i < t.size()-p.size()+1; i++){
        if(stoll(t.substr(i,p.size())) <= stoll(p)){
            answer+=1;
        }
    }
    return answer;
}