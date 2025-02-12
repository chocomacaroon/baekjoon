#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    for(int i = 0; i < strArr.size(); i++){
        string tmp = "";
        if(i%2 == 0){
            for(int j = 0; j < strArr[i].size(); j++){
                tmp += tolower(strArr[i][j]);
            }
            answer.push_back(tmp);
        }
        else{
            for(int j = 0; j < strArr[i].size(); j++){
                tmp += toupper(strArr[i][j]);
            }
            answer.push_back(tmp);
        }
    }
    return answer;
}