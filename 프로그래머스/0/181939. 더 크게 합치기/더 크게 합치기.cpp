#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    if(to_string(a)+to_string(b) > to_string(b)+to_string(a)){
        return stoi(to_string(a)+to_string(b));
    }
    else{
        return stoi(to_string(b)+to_string(a));
    }
    return answer;
}