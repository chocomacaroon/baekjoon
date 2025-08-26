#include <string>
#include <vector>

using namespace std;

int solution(string word) {
    int answer = 0;
    string str = "AEIOU";
    int jumps[] = {781, 156, 31, 6, 1};
    
    for(int i = 0; i < word.length(); i++){
        int n = str.find(word[i]);
        answer += n*jumps[i]+1;
    }
    return answer;
}