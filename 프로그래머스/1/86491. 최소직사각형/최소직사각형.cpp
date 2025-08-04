#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int h = 0;
    int w = 0;
    int n1, n2;
    for(int i = 0; i < sizes.size(); i++){
        n1 = sizes[i][0];
        n2 = sizes[i][1];
        if(n1>n2) swap(n1,n2);
        if(h < n1) h = n1;
        if(w < n2) w = n2;
    }
    return w*h;
}