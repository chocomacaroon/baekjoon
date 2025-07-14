#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n) {
    int answer = n;
    string bin = "";
    while(n>0){
        bin += to_string(n%2);
        n/=2;
    }
    
    int cnt_one = count(bin.begin(), bin.end(), '1');
    
    while(1){
        answer+=1;
        string bin = "";
        int n = answer;
        while(n > 0){
            bin += to_string(n%2);
            n /= 2;
        }
        if(count(bin.begin(), bin.end(), '1') == cnt_one)
            return answer;
    }
    return answer;
}