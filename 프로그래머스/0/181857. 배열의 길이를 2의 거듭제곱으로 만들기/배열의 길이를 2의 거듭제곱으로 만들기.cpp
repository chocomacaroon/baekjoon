#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int n = 1;
    while(n < arr.size()){
        n *= 2;
    }
    for(auto num:arr){
        answer.push_back(num);
    }
    for(int i = arr.size(); i < n; i++){
        answer.push_back(0);
    }
    return answer;
}