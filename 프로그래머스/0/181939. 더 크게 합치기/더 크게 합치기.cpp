#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    if(stoi(to_string(a)+to_string(b)) > stoi(to_string(b)+to_string(a))){
        return stoi(to_string(a)+to_string(b));
    }
    else{
        return stoi(to_string(b)+to_string(a));
    }
}