#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int y2;
    for(int y1 = 1; y1 <= yellow; y1++){
        if(yellow%y1 == 0){
            y2 = yellow/y1;
            if(2*y1+2*y2 + 4 == brown){
                return {y2+2, y1+2};
            }
        }
    }
    return answer;
}