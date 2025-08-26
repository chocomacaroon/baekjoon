#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int solution(string dirs) {
    int answer = 0;
    set <vector<int>> visited;
    int x = 0;
    int y = 0;
    
    for (auto com : dirs){
        int nx=x;
        int ny=y;
        if (com == 'U'){
            if (ny+1 <= 5)
                ny += 1;
        }
        else if (com == 'D'){
            if (ny-1 >= -5)
                ny -= 1;
        }
        else if (com == 'R'){
            if (nx+1 <= 5)
                nx += 1;
        }
        else if (com == 'L'){
            if (nx-1 >= -5)
                nx -= 1;
        }
        if (x != nx || y != ny){
            if (x < nx || (x == nx && y < ny))
                visited.insert({x,nx,y,ny});
            else{
                visited.insert({nx,x,ny,y});
            }
        }
        x = nx;
        y = ny;
    }
    return visited.size();
}