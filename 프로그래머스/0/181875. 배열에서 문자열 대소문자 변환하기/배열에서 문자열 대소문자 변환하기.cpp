#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    for(int i = 0;i < strArr.size(); i++){
        if(i%2==0){
            transform(strArr[i].begin(), strArr[i].end(), strArr[i].begin(), ::tolower);
        }
        else{
            transform(strArr[i].begin(), strArr[i].end(), strArr[i].begin(), ::toupper);
        }
        answer.push_back(strArr[i]);
    }
    return answer;
}