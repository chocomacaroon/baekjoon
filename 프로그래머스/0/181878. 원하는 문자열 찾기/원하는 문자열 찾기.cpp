#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    for(int i = 0; i < myString.size(); i++){
        myString[i] = tolower(myString[i]);
    }
    for(int j = 0; j < pat.size(); j++){
        pat[j] = tolower(pat[j]);
    }
    if(myString.find(pat)==string::npos){
        return 0;
    }
    else{
        return 1;
    }
    return answer;
}