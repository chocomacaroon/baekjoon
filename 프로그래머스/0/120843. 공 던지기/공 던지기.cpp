#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int k) {
    int answer = 0;
    for(int i = 0; i < k-1; i++){
        answer += 2;
    }
    return numbers[answer % numbers.size()];
}