#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    long long ptmp = 0;
    for(int i = 0; i < p.size(); i++){
        ptmp = ptmp*10+(p[i]-'0');
    }
    for(int i = 0; i < t.size()-p.size()+1; i++){
        long long tmp = 0;
        for(int j = i; j < i+p.size(); j++){
            tmp = tmp*10 + (t[j]-'0');
        }
        if(tmp <= ptmp){
            answer+=1;
        }  
    }
    return answer;
}