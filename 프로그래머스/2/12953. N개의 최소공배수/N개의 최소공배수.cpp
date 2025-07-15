#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b){
    int c;
    while(b!=0){
        c = a%b;
        a = b;
        b = c;
    }
    return a;
}

int lcm(int a, int b){
    return a*b/gcd(a,b);
}
int solution(vector<int> arr) {
    int answer = 1;
    for(int n:arr){
        answer = lcm(n, answer);
    }
    return answer;
}