#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int w = 0;
    int h = 0;
    int min = 0;
    int max = 0;
    for(int i = 0; i < sizes.size(); i++){
        if(sizes[i][0] > sizes[i][1]){
            max = sizes[i][0];
            min = sizes[i][1];
        }
        else{
            max = sizes[i][1];
            min = sizes[i][0];
        }
        if(min > w){
            w = min;
        }
        if(max > h){
            h = max;
        }
    }
    return w*h;
}