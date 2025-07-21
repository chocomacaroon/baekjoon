#include <string>
#include <vector>

using namespace std;
int ans = 0;

void dfs(int pos, int sum, vector<int> numbers, int target){
    if(pos == numbers.size()){
        if(sum == target) ans+=1;
        return;
    }
    dfs(pos+1, sum + numbers[pos], numbers, target);
    dfs(pos+1, sum - numbers[pos], numbers, target);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(0, 0, numbers, target);
    return ans;
}