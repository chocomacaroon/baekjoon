#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> wallet, vector<int> bill) {
    int answer = 0;
    int big, small;
    if(bill[0] > bill[1]){
        big = bill[0];
        small = bill[1];
    }
    else{
        big = bill[1];
        small = bill[0];
    }
    sort(wallet.begin(), wallet.end());
    while(1){
        if(big <= wallet[1] && small <= wallet[0])
            break;
        big /= 2;
        if(big < small){
            int tmp = small;
            small = big;
            big = tmp;
        }
        answer++;
    }
    return answer;
}