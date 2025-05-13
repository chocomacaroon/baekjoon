#include <string>
#include <vector>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "";
    int idx1 = 0;
    int idx2 = 0;
    for(int i = 0; i < goal.size(); i++){
        if(cards1.front() == goal[i]){
            cards1.erase(cards1.begin());
        }
        else if(cards2.front() == goal[i]){
            cards2.erase(cards2.begin());
        }
        else{
            return "No";
        }
    }
    return "Yes";
}