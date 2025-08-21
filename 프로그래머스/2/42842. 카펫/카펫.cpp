#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int w;
    int h;
    for(int w = 3; w <= brown/2; w++){
        h = brown/2-w + 2;
        if ((w-2)*(h-2) == yellow){
            return {h, w};
        }
    }
    return answer;
}