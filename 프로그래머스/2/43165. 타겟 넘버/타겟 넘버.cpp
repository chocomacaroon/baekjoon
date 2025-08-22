#include <string>
#include <vector>

using namespace std;

int dfs(int sum, int pos, vector<int> numbers, int target){
    if(pos == numbers.size()){
        if(sum == target){
            return 1;
        }
        return 0;
    }
    return dfs(sum-numbers[pos], pos+1, numbers, target) + dfs(sum+numbers[pos], pos+1, numbers, target);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    return dfs(0, 0, numbers, target);
}