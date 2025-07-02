#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//연속해서x

int solution(vector<string> babbling) {
    int answer = 0;
    vector<string> can = {"aya", "ye", "woo", "ma"};
    string tmp = "";
    string before = "";
    for(string b:babbling){
        tmp = "";
        before = "";
        for(auto c:b){
            tmp+=c;
            if(find(can.begin(), can.end(),tmp) !=can.end()){
                if(before == tmp){
                    break;
                }
                before = tmp;
                tmp = "";
            }
        }
        if(tmp.empty() || find(can.begin(), can.end(),tmp) !=can.end()){
            if(before!=tmp){
                answer+=1;
            }
        }
    }
    return answer;
}