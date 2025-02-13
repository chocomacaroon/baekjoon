#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int num, int k) {
    if(to_string(num).find(to_string(k))==-1){
        return to_string(num).find(to_string(k));
    }
    return to_string(num).find(to_string(k))+1;
}