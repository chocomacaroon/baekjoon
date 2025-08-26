#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(int n, int t, int m, int p) {
    string answer = "";
    string res = "";
    vector<char> nums = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    int x = 0;
    while (res.size() <= m*t){
        int x2 = x;
        string s = "";
        while(x2){
            s += nums[x2 % n];
            x2 /= n;
        }
        reverse(s.begin(), s.end());
        if(s=="") s="0";
        for (auto c:s){
            res += c;
        }
        x+=1;
    }
    int i = p-1;
    while (answer.size() < t){
        answer.push_back(res[i]);
        i+=m;
    }
    return answer;
}