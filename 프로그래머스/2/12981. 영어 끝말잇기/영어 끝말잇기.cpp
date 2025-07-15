#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer = {0, 0};
    vector<string> box;
    box.push_back(words[0]);
    
    for(int i = 1; i < words.size(); i++){
        if(find(box.begin(), box.end(), words[i])!=box.end() || words[i][0] != box[i-1][box[i-1].size()-1]){
            return {i%n+1, i/n+1};
        }
        
        box.push_back(words[i]);
        
    }

    return answer;
}