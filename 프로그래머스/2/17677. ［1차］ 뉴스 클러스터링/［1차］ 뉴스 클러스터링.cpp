#include <string>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int solution(string str1, string str2) {
    int answer = 0;
    vector<string> s1;
    vector<string> s2;
    for(int i = 0; i < str1.size(); i++){
        if(isalpha(str1[i]) && isalpha(str1[i+1])){
            string s;
            s += tolower(str1[i]);
            s += tolower(str1[i+1]);
            s1.push_back(s);
        }
            
    }
    for(int i = 0; i < str2.size(); i++){
        if(isalpha(str2[i]) && isalpha(str2[i+1])){
            string s;
            s += tolower(str2[i]);
            s += tolower(str2[i+1]);
            s2.push_back(s);
        }
    }
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    vector<string> result;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(result));
    vector<string> result2;
    set_union(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(result2));
    if(result2.size() == 0) return 65536;
    return int(result.size()/(double)result2.size()*65536);
    return answer;
}