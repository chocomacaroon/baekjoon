#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int zero_cnt = 0;
    int times = 0;
    while(s != "1"){
        times += 1;
        zero_cnt += count(s.begin(), s.end(), '0');
        s.erase(remove(s.begin(), s.end(), '0'), s.end());
        int len = s.length();
        s = "";
        while(len > 0){
            s += to_string(len % 2);
            len /= 2;
        }
    }
    answer = {times, zero_cnt};
    return answer;
}