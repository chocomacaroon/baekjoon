#include <string>
#include <vector>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "Yes";
    int a = 0;
    int b = 0;
    
    for(int i = 0; i < goal.size(); i++){
        if(cards1[a] == goal[i]){
            a+=1;
        }
        else if(cards2[b] == goal[i]){
            b+=1;
        }
        else{
            return "No";
        }
    }
    return answer;
}