#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, int k) {
    int answer = 0;
    int x = 0;
    int y = 0;
    for(int x = 0; x < board.size(); x++){
        for(int y = 0; y < board[0].size(); y++){
            if(x+y<=k)
                answer += board[x][y];
        }
    }
    return answer;
}