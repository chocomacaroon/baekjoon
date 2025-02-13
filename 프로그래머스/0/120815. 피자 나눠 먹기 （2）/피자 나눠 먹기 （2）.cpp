#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = n;
    while(1){
        if(answer%6==0){
            return answer/6;
        }
        answer+=n;
    }
}