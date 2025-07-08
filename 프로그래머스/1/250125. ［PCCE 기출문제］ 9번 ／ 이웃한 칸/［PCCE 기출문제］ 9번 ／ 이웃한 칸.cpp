#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<string>> board, int h, int w) {
    int answer = 0;
    string target = board[h][w];
    if(0 <= h-1){
        if(board[h-1][w] == target){
            answer+=1;
        }
    }
    if(h+1 < board.size()){
        if(board[h+1][w] == target){
            answer+=1;
        }
    }
    if(0 <= w-1){
        if(board[h][w-1] == target){
            answer+=1;
        }
    }
    if(w+1 < board.size()){
        if(board[h][w+1] == target){
            answer+=1;
        }
    }
    return answer;
}