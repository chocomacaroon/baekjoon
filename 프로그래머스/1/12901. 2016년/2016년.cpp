#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    int days = b;
    vector<int> m_days({31,29,31,30,31,30,31,31,30,31,30,31});
    vector<string> day({"MON","TUE","WED","THU","FRI","SAT","SUN"});
    for(int i = 0; i < a-1; i++){
        days+=m_days[i];
    }
    return day[(days+3)%7];
}