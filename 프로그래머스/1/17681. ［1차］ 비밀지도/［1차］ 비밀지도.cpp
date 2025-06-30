#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<string> ans1;
    vector<string> ans2;
    string tmp;
    
    for(int i = 0; i < n; i++){
        int k = arr1[i];
        tmp = "";
        while(k>0){
            tmp += to_string(k%2);
            k = k / 2;
        }
        while(tmp.size() < n) tmp += '0';
        reverse(tmp.begin(), tmp.end());
        ans1.push_back(tmp);
    }
    
    for(int i = 0; i < n; i++){
        int k = arr2[i];
        string tmp = "";
        while(k>0){
            tmp += to_string(k%2);
            k = k / 2;
        }
        while(tmp.size() < n) tmp += '0';
        reverse(tmp.begin(), tmp.end());
        ans2.push_back(tmp);
    }
    
    for(int i = 0; i < n; i++){
        tmp = "";
        for(int j = 0; j < n; j++){
            if(ans1[i][j] == '1' || ans2[i][j] == '1'){
                tmp += '#';
            }
            else{
                tmp += ' ';
            }
        }
        answer.push_back(tmp);
    }
    return answer;
}