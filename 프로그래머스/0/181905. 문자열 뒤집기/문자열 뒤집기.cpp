#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string, int s, int e) {
    string answer = "";
    answer += my_string.substr(0,s);
    string tmp = my_string.substr(s,e-s+1);
    reverse(tmp.begin(), tmp.end());
    answer += tmp;
    answer += my_string.substr(e+1,my_string.size()-e+1);
    return answer;
}