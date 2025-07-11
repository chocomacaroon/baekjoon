#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;
    vector<vector<int>> res;
    vector<string> std = {"code", "date","maximum","remain"};
    int idx_ext = find(std.begin(), std.end(), ext) - std.begin();
    int idx_sort = find(std.begin(), std.end(), sort_by) - std.begin();
    for(int i = 0; i < data.size(); i++){
        if(data[i][idx_ext] <= val_ext){
            res.push_back(data[i]);
        }
    }
    sort(res.begin(), res.end(), [idx_sort](vector<int> &a, vector<int> &b){return a[idx_sort] < b[idx_sort];});
    return res;
}