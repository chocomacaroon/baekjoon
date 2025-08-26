#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool isPrime(long long n){
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n%2==0) return false;
    for (long long i = 3; i * i <= n; i+=2){
        if (n%i==0) return false;
    }
    return true;
}

int solution(int n, int k) {
    int answer = 0;
    string res = "";
    while(n){
        res += to_string(n%k);
        n/=k;
    }
    reverse(res.begin(), res.end());
    string tmp = "";
    for (char c:res){
        if (c == '0'){
            if (tmp != ""){
                if(isPrime(stoll(tmp))){
                    answer+=1;
                }
                tmp = "";
            }
        }
        else{
            tmp += c;
        }
    }
    if(tmp!=""&&isPrime(stoll(tmp))){
        answer+=1;
    }
    return answer;
}