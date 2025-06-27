#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    string str = "";
    int n;
    int cnt = 0;
    int delet = 0;
    while(s !="1"){
        cnt += 1;
        string bin = "";
        n = count(s.begin(), s.end(), '1');
        delet += s.size()-n;
        while(n>0){
            bin += to_string(n%2);
            n/=2;
        }
        reverse(bin.begin(), bin.end());
        s = bin;
    }
    answer = {cnt, delet};
    return answer;
}