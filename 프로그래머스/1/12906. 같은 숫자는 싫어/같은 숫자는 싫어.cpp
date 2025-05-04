#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    
    for(auto c : arr){
        if(answer.empty() or answer.back()!=c){
            answer.push_back(c);
        }
    }
    return answer;
}