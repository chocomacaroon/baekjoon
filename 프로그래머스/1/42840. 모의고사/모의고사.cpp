#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> tmp;
    vector<int> ans1({1,2,3,4,5});
    vector<int> ans2({2,1,2,3,2,4,2,5});
    vector<int> ans3({3,3,1,1,2,2,4,4,5,5});
    int score1 = 0;
    int score2 = 0;
    int score3 = 0;
    for(int i = 0; i < answers.size(); i++){
        if(answers[i]==ans1[i%ans1.size()])
            score1++;
        if(answers[i]==ans2[i%ans2.size()])
            score2++;
        if(answers[i]==ans3[i%ans3.size()])
            score3++;
    }
    tmp.push_back(score1);
    tmp.push_back(score2);
    tmp.push_back(score3);
    int m = *max_element(tmp.begin(), tmp.end());
    for(int i = 0; i < tmp.size(); i++){
        if(tmp[i]==m){
            answer.push_back(i+1);
        }
    }
    return answer;
}