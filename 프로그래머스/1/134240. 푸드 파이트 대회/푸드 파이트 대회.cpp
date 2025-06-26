#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> food) {
    string answer = "";
    string tmp = "";
    for(int i = 0; i < food.size(); i++){
        for(int j = 0; j < food[i]/2; j++){
            tmp += to_string(i);
        }
    }
    answer = tmp + '0';
    reverse(tmp.begin(), tmp.end());
    answer += tmp;
    return answer;
}