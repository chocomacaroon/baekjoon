#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = citations.size();
    sort(citations.begin(), citations.end(), greater<int>());
    
    for(int i = 0; i < citations.size(); i++){
        if(i >= citations[i]){
            return i;
        }
    }
    return answer;
}

// 3 0 6 1 5

//입력값 〉 [5, 6, 7, 8]
// 기댓값 〉 4

// 8 7 6 5
