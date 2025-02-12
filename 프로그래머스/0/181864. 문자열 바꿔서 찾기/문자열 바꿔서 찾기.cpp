#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    string inverse = "";
    for(int i = 0; i < myString.size(); i++){
        if(myString[i] == 'A'){
            inverse += 'B';
        }
        else if(myString[i] == 'B'){
            inverse += 'A';
        }
    }
    if(inverse.find(pat) != string::npos){
        return 1;
    }
    else{
        return 0;
    }
}