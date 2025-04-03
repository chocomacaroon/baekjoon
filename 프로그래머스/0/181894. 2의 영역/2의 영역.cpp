#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int s = find(arr.begin(), arr.end(), 2) - arr.begin();
    vector<int> rev = arr;
    reverse(rev.begin(), rev.end());
    int e = find(rev.begin(), rev.end(),2) - rev.begin();
    for(int i = s; i < arr.size()-e;i++){
        answer.push_back(arr[i]);
    }
    if(answer.size()==0){
        answer.push_back(-1);
    }
    return answer;
}