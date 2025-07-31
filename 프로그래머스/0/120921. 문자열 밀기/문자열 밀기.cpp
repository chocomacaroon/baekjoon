#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string A, string B) {
    int answer = -1;
    for(int i = 0; i < A.size(); i++){
        string tmp = A.substr(A.size()-i, i);
        tmp += A.substr(0,A.size()-i);
        cout << tmp << endl;
        if(tmp == B) return i;
    }
    return answer;
}