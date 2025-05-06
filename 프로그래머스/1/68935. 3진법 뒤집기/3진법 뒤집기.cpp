#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = 0;
    string thr = "";
    while(n>0){
        thr += to_string(n%3);
        n /= 3;
    }
    // answer = stoi(thr);
    // return answer;
    reverse(thr.begin(), thr.end());
    // return stoi(thr);
    for(int i = 0; i < thr.size(); i++){
        answer += (thr[i]-'0')*(pow(3,i));
    }
    return answer;
}