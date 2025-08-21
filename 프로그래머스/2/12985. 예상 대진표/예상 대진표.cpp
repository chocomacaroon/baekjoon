#include <iostream>
#include <vector>

using namespace std;

int solution(int n, int a, int b)
{
    int round = 0;
    vector<int> v;
    for(int i = 1; i <= n; i++){
        v.push_back(i);
    }
    while(1){
        round += 1;
        vector<int> tmp;
        for(int i = 0; i < v.size(); i+=2){
            if ((v[i] == a && v[i+1] == b) ||(v[i] == b && v[i+1] == a)){
                return round;
            }
            else if(v[i] == a || v[i] == b){
                tmp.push_back(v[i]);
            }
            else if(v[i+1] == a || v[i+1] == b){
                tmp.push_back(v[i+1]);
            }
            else{
                tmp.push_back(v[i]);
            }
        }
        v = tmp;
    }
    return round;
}