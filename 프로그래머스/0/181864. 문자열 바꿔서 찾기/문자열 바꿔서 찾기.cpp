#include <string>
#include <vector>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    string new_string = "";
    for(auto c:myString){
        if(c == 'A'){
            new_string += "B";
        }
        else if(c == 'B'){
            new_string += "A";
        }
    }
    if(new_string.find(pat) != string::npos){
        return 1;
    }
    return answer;
}