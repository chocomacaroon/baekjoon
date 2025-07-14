#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer;
    int posx = 0;
    int posy = 0;
    for(int i = 0; i < park.size(); i++){
        if(park[i].find('S') != string::npos){
            posx = i;
            posy = park[i].find('S');
        }
    }
    for(string s:routes){
        char dir = s[0];
        int dis = s[2]-'0';
        bool flag = true;
        if(dir == 'E'){
            if(posy + dis < park[0].size()){
                int y = posy;
                while(y < posy+dis){
                    y+=1;
                    if(park[posx][y] == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag){
                    posy += dis;
                }  
            }
        }
        else if(dir == 'W'){
            if(posy - dis >= 0){
                int y = posy;
                while(y > posy-dis){
                    y-=1;
                    if(park[posx][y] == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag){
                    posy-= dis;
                }  
            }
        }
        else if(dir == 'S'){
            if(posx + dis < park.size()){
                int x = posx;
                while(x < posx+dis){
                    x+=1;
                    if(park[x][posy] == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag)
                    posx += dis;
            }
        }
        else if(dir == 'N'){
            if(posx - dis >= 0){
                int x = posx;
                while(x > posx-dis){
                    x-=1;
                    if(park[x][posy] == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag)
                    posx -= dis;
            }
        }
    }
    answer = {posx, posy};
    return answer;
}