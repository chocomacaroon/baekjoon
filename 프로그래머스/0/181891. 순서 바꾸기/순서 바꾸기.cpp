#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> num_list, int n) {
    vector<int> answer;
    for(int i = 0; i < n; i++){
        rotate(num_list.begin(), num_list.begin()+1, num_list.end());
    }
    return num_list;
}