#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(string X, string Y) {
    string answer = "";
    vector<char> v1;
    vector<char> v2;
    vector<char> v3;
    for(char c:X) v1.push_back(c);
    for(char c:Y) v2.push_back(c);
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(),  back_inserter(v3));
    if(v3.empty()) return "-1"; 
    for(auto c:v3) answer += c;
    reverse(answer.begin(), answer.end());
    if(answer[0]=='0') return "0";
    return answer;
}