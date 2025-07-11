#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<vector<int>> column;
    for(int i = 0; i < board.size(); i++){
        vector<int> tmp;
        for(int j = board[0].size()-1; j >= 0 ; j--){
            if(board[j][i]!=0)
                tmp.push_back(board[j][i]);
        }
        column.push_back(tmp);
    }
    // for(int i = 0; i < column.size(); i++){
    //     for(int n:column[i])
    //         cout << " ";
    //     cout << endl;
    // }
    vector<int> stk;
    for(int n:moves){
        if(!column[n-1].empty()){
            if(!stk.empty() && stk.back() == column[n-1].back()){
                stk.pop_back();
                column[n-1].pop_back();
                answer+=2;
            }
            else{
                stk.push_back(column[n-1].back());
                column[n-1].pop_back();
                
            }
        }        
        else{
            stk.push_back(column[n-1].back());
            column[n-1].pop_back();
        }
    }
    return answer;
}