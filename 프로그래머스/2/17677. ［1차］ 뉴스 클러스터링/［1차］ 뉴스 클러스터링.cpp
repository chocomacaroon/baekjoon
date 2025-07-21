#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <cctype>

using namespace std;

int solution(string str1, string str2) {
    int answer = 0;
    
    vector<string> a;
    vector<string> b;
    
    for(int i = 0; i < str1.size()-1; i++){
        char c1 = str1[i];
        char c2 = str1[i+1];
        if(isalpha(c1)&&isalpha(c2)){
            string s;
            s += tolower(c1);
            s += tolower(c2);
            a.push_back(s);
        }
    }
    for(int i = 0; i < str2.size()-1; i++){
        char c1 = str2[i];
        char c2 = str2[i+1];
        if(isalpha(c1)&&isalpha(c2)){
            string s;
            s += tolower(c1);
            s += tolower(c2);
            b.push_back(s);
        }
    }
    
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    
    vector<string> v_union;
    vector<string> v_intersection;
    
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), back_inserter(v_intersection));
    set_union(a.begin(), a.end(), b.begin(), b.end(), back_inserter(v_union));
    if(v_union.size()==0) return 65536;
    return (int)((double)v_intersection.size() / v_union.size() * 65536);
}

//J(A,B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.