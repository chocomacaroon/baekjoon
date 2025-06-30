#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> n1 = {1,2,3,4,5};
    vector<int> n2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> n3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    vector<int> score(3);
    for(int i = 0; i < answers.size(); i++){
        if(answers[i] == n1[i%n1.size()])
            score[0]+=1;
        if(answers[i] == n2[i%n2.size()])
            score[1]+=1;
        if(answers[i] == n3[i%n3.size()])
            score[2]+=1;
    }
    
    int max = *max_element(score.begin(), score.end());
    for(int i = 0 ; i < 3; i++){
        if(max == score[i])
            answer.push_back(i+1);
    }
    return answer;
}