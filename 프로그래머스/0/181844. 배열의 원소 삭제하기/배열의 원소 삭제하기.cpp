#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, vector<int> delete_list) {
    vector<int> answer;
    for(auto n:delete_list){
        arr.erase(remove(arr.begin(), arr.end(),n),arr.end());
    }
    return arr;
}