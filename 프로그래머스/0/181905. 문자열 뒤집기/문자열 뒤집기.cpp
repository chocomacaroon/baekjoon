#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string, int s, int e) {
    string answer = "";
    string rev = my_string.substr(s,e-s+1);
    reverse(rev.begin(),rev.end());
    answer = my_string.substr(0,s) + rev + my_string.substr(e+1,my_string.size());
    
    return answer;
}