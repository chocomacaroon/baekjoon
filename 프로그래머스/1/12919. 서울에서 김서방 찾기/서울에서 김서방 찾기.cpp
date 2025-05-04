#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    int n = distance(seoul.begin(),find(seoul.begin(), seoul.end(), "Kim"));
    return "김서방은 "+to_string(n)+"에 있다";
}