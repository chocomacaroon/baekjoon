#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    map<char,int> doc;
    for(int i = 0; i < terms.size(); i++){
        doc[terms[i][0]] = stoi(terms[i].substr(2));
    }
    
    int total_today = stoi(today.substr(0,4))*12*28+stoi(today.substr(5,2))*28+stoi(today.substr(8,2));
    for(int i = 0; i < privacies.size(); i++){
        
        int deadline = doc[privacies[i][privacies[i].size()-1]];
        int year = stoi(privacies[i].substr(0,4));
        int month = stoi(privacies[i].substr(5,2));
        int day = stoi(privacies[i].substr(8,2));
        
        int total = year * 12 * 28 + month *28 + day + deadline*28 - 1;
        
        
        if(total_today > total){
            answer.push_back(i+1);
        }
    }
    return answer;
}