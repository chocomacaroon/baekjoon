#include <string>
#include <vector>

using namespace std;

int solution(string str1, string str2) {
    int answer = 0;
    if(str2.find(str1) != -1){
        return 1;
    }
    else{
        return 0;
    }
    return answer;
}