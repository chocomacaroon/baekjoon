#include <string>
#include <vector>
#include <sstream>

using namespace std;

string solution(string s) {
    string answer = "";
    stringstream ss(s);
    int num;
    ss >> num;
    int max_val = num;
    int min_val = num;
    while (ss >> num){
        if (num < min_val){
            min_val = num;
        }
        if (num > max_val){
            max_val = num;
        }
    }
    answer = to_string(min_val) + " " + to_string(max_val);
    return answer;
}