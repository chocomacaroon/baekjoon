#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int i = 0;
    while(i < arr.size()){
        if(answer.size() == 0){
            answer.push_back(arr[i]);
            i++;
        }
        else if(answer.back() == arr[i]){
            answer.pop_back();
            i++;
        }
        else if(answer.back() != arr[i]){
            answer.push_back(arr[i]);
            i++;
        }
    }
    if(answer.size()==0){
        answer.push_back(-1);
    }
    return answer;
}