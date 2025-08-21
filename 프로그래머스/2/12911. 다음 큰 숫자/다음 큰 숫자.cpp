#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n) {
    int answer = 0;
    string s = "";
    int num = n;
    while(num>0){
        s += to_string(num%2);
        num /= 2;
    }
    int target = count(s.begin(), s.end(), '1');
    while(1){
        n+=1;
        s = "";
        int num = n;
        while(num>0){
            s += to_string(num%2);
            num /= 2;
        }
        int cnt = count(s.begin(), s.end(), '1');
        if (cnt == target){
            return n;
        }
    }
    return answer;
}