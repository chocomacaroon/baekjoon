#include <string>
#include <vector>

using namespace std;
vector<int> days = {0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
vector<string> res = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
string solution(int a, int b) {
    string answer = "";
    int tday = b;
    for(int i = 1; i < a; i++){
        tday += days[i];
    }
    return res[(tday+4)%7];
}