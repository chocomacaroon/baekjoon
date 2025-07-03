#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    string tmp = "";
    char domain;
    int i = 0;
    vector<int> num;
    for(char c:dartResult){
        if(isdigit(c)){
            tmp += c;
        }
        else if(isalpha(c)){
            if(c=='S'){
                num.push_back(stoi(tmp));
                tmp = "";
            }
            else if(c == 'D'){
                num.push_back(stoi(tmp)*stoi(tmp));
                tmp = "";
            }
            else if(c == 'T'){
                num.push_back(stoi(tmp)*stoi(tmp)*stoi(tmp));
                tmp = "";
            }
            i+=1;
        }
        else if(c == '*'){
            num[i-1] = num[i-1] * 2;
            if(i-2>=0){
                num[i-2] = num[i-2] * 2;
            }
            
        }
        else if(c == '#'){
            num[i-1] = -num[i-1];
        }
    }
    answer = accumulate(num.begin(), num.end(), 0);
    return answer;
}