#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    int left = 0;
    int right = people.size()-1;
    
    while(left <= right){
        if(people[left]+people[right] <= limit){
            left+=1;
            right-=1;
            answer+=1;
        }
        else{
            answer+=1;
            right-=1;
        }
    }
    return answer;
}

//50 50 70 80