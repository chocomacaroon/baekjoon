#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> stk;
    int i = 0;
    while(i < arr.size()){
        if(stk.empty()){
            stk.push_back(arr[i]);
            i+=1;
        }
        else{
            if(stk.back() == arr[i]){
                stk.pop_back();
                i+=1;
            }
            else{
                stk.push_back(arr[i]);
                i+=1;
            }
        }
    }
    if(stk.empty()) return {-1};
    return stk;
}