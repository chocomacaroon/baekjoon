#include <iostream>
using namespace std;

int solution(int n)
{
    int ans = 0;
    if (n%2==1){
        ans += 1;
        n -= 1;
    }
    while(n > 0){
        n /= 2;
        if(n%2){
            ans += n%2;
        }
    } 
    return ans;
}
