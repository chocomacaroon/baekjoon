#include <string>
#include <vector>

using namespace std;

string solution(string myString, string pat) {
    string answer = "";
    for(int i = 0; i < myString.size()-pat.size()+1; i++){
        if(myString.substr(myString.size()-pat.size()-i,pat.size()) == pat){
            return myString.substr(0,myString.size()-i);
        }
    }
    return answer;
}