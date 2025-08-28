#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b){
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> s_numbers;
    
    for(int num : numbers){
        s_numbers.push_back(to_string(num));
    }
    
    sort(s_numbers.begin(), s_numbers.end(), compare);
    
    for(string s_num : s_numbers){
        answer += s_num;
    }
    if(answer[0] == '0'){
        return "0";
    }
    return answer;
}