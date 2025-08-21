#include <string>
#include <vector>
#include <numeric>

using namespace std;

int lcm(int n1, int n2){
    return (n1*n2)/gcd(n1, n2);
}

int solution(vector<int> arr) {
    int answer = 0;
    int num = arr[0];
    for(int i = 1; i < arr.size(); i++){
        num = lcm (num, arr[i]);
    }
    return num;
}