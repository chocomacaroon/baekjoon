#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = "";
    string age_str = to_string(age);
    for(auto c:age_str){
        answer += 'a'+c-'0';
    }
    return answer;
}