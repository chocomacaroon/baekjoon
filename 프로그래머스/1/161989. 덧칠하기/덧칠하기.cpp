#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    int pos = 1;
    for(int i = 0; i < section.size(); i++){
        if(pos <= section[i]){
            pos = section[i] + m;
            answer+=1;
        }
    }
    return answer;
}