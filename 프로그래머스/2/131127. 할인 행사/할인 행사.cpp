#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map <string, int> m;
    for (int i = 0; i < want.size(); i++){
        m[want[i]] = number[i];
    }
    
    for (int i = 0; i <= discount.size()-10; i++){
        map <string, int> discount_m;
        for (int j = i; j < i+10; j++){
            discount_m[discount[j]]+=1;
        }
        bool is_possible = true;
        for (auto [item, count] : m){
            if(discount_m.find(item) == discount_m.end() || discount_m[item] < count){
                is_possible = false;
                break;
            } 
        }
        if(is_possible) answer+=1;
    }
    return answer;
}