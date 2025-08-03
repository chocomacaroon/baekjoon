#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int n = 0;
    int num = x;
    while(x>0){
        n += (x%10);
        x /= 10;
    }
    return (num % n == 0) ? true : false;
}