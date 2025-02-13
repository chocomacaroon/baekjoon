#include <string>
#include <vector>

using namespace std;

string solution(string n_str) {
    int i;
    for(i = 0; i < n_str.size(); i++){
        if(n_str[i] != '0'){
            break;
        }
    }
    return n_str.substr(i,n_str.size()-i);
}