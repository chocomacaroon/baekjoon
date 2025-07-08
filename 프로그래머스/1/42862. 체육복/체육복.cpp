#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> v(n, 1);
    for(int a : reserve)
        v[a-1] = 2;
    for(int b : lost)
        v[b-1] -= 1;
    if(v[1]>1 && v[0] == 0){
        v[0]+=1;
        v[1]-=1;
    }
    for(int i = 1; i < n-1; i++){
        if(v[i]==0){
            if(v[i-1]>1){
                v[i]+=1;
                v[i-1]-=1;
            }
            else if(v[i+1]>1){
                v[i]+=1;
                v[i+1]-=1;
            }  
        }
    }
    if(v[n-2]>1 && v[n-1] == 0){
        v[n-1]+=1;
        v[n-2]-=1;
    }
    answer = n - count(v.begin(), v.end(), 0);
    return answer;
}

// 1 1 0 2