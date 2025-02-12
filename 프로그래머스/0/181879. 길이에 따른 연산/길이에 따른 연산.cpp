#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    if(num_list.size() >= 11){
        int sum = 0;
        for(int i = 0; i < num_list.size(); i++){
            sum += num_list[i];
        }
        return sum;
    }
    else{
        int sub = 1;
        for(int i = 0; i < num_list.size(); i++){
            sub *= num_list[i];
        }
        return sub;
    }
}