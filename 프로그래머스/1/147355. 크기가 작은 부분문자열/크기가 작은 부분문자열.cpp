#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int sz = p.size();
    for(int i = 0; i < t.size() - sz + 1; i++){
        if(stol(t.substr(i, sz)) <= stol(p)) answer+=1;
    }
    return answer;
}