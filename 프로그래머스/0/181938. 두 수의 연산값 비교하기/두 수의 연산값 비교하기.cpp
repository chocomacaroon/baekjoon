#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    if(stoi(to_string(a)+to_string(b)) > 2*a*b){
        return stoi(to_string(a)+to_string(b));
    }
    else{
        return 2*a*b;
    }
    return answer;
}