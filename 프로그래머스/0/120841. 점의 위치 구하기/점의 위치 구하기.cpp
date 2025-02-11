#include <string>
#include <vector>

using namespace std;

int solution(vector<int> dot) {
    int x = dot[0];
    int y = dot[1];
    if(x > 0 and y > 0){
        return 1;
    }
    else if(x < 0 and y > 0){
        return 2;
    }
    else if(x < 0 and y < 0){
        return 3;
    }
    else if(x > 0 and y < 0){
        return 4;
    }
}