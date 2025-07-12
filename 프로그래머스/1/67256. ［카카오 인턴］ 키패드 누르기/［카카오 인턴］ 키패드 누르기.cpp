#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    vector<int> l_pos = {-1, 0};
    vector<int> r_pos = {1, 0};
    
    for(int n:numbers){
        if(n==1||n==4||n==7){
            answer+="L";
            if(n == 1){
                l_pos = {-1, 3};
            }
            if(n == 4){
                l_pos = {-1, 2};
            }
            if(n == 7){
                l_pos = {-1, 1};
            }
        }
        else if(n==3||n==6||n==9){
            answer+="R";
            if(n == 3){
                r_pos = {1, 3};
            }
            if(n == 6){
                r_pos = {1, 2};
            }
            if(n == 9){
                r_pos = {1, 1};
            }
        }
        else{
            vector<int> npos;
            if(n==2){
                npos = {0, 3};   
            }
            else if(n==5){
                npos = {0, 2};   
            }
            else if(n==8){
                npos = {0, 1};   
            }
            else if(n == 0){
                npos = {0, 0};
            }
            int ldistance = abs(l_pos[0]-npos[0]) + abs(l_pos[1]-npos[1]);
            int rdistance = abs(r_pos[0]-npos[0]) + abs(r_pos[1]-npos[1]);
            if(ldistance<rdistance){
                answer+="L";
                l_pos = npos;
            }
            else if(ldistance>rdistance){
                answer+="R";
                r_pos = npos;
            }
            else{
                if(hand == "right"){
                    answer += "R";
                    r_pos = npos;
                }
                else{
                    answer += "L";
                    l_pos = npos;
                }
            }
        }
    }
    return answer;
}
