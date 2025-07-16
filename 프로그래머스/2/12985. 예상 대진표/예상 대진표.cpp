#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n, int a, int b)
{
    int ground = 0;
    vector<int> next;
    for(int i = 1; i <= n; i++)
        next.push_back(i);
    
    for(int j = 0; j < sqrt(n); j++){
        ground += 1;
        vector<int> now = next;
        next = {};        
        for(int i = 0; i < now.size(); i+=2){
            if((now[i] == a && now[i+1] == b) || (now[i] == b && now[i+1] == a)){
                return ground;
            }
            else if(now[i] == a || now[i] == b){
                next.push_back(now[i]);
            }
            else if(now[i+1] == a || now[i+1] == b){
                next.push_back(now[i+1]);
            }
            else{
                next.push_back(now[i]);
            }
        }
    }
    return ground;
}