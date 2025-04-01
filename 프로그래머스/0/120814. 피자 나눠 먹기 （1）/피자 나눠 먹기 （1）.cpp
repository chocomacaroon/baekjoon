#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    return n/7+int(bool(n%7));
}