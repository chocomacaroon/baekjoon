#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    set<int> S;
    for(int i = 0; i < numbers.size()-1; i++)
        for(int j = i+1; j< numbers.size(); j++){
            S.insert(numbers[i]+numbers[j]);
        }
    answer.assign(S.begin(), S.end());
    return answer;
}