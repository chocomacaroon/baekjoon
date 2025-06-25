#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b){
    int tmp;
    while(b){
        tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}
vector<int> solution(int n, int m) {
    vector<int> answer;
    return {gcd(n,m), (n*m)/(gcd(n,m))};
    return answer;
}