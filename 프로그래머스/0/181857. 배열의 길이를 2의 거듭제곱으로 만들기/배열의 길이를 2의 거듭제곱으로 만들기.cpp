#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    
    int n = 1;
    
    while(1){
       if(n >= arr.size()){
           break;
       }
        n *= 2;
   }
    
    for(int i = 0; i < arr.size(); i++){
        answer.push_back(arr[i]);
    }
   
    for(int i = 1; i <= n-arr.size();i++){
        answer.push_back(0);
    }
    return answer;
}