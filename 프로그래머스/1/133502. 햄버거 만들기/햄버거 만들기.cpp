#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;
    vector<int> v;
    string s = "";
    for(int i : ingredient){
        s += to_string(i);
    }
    while(s.find("1231") != string::npos){
        answer+=1;
        s.erase(s.find("1231"), 4);
    }
    return answer;
}