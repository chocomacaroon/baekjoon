#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(vector<int> elements) {
    int answer = 0;
    set<int> s;
    for(int i = 1; i <= elements.size(); i++){
        int sum = 0;
        for(int j = 0; j < elements.size(); j++){
            if(j+i >= elements.size()){
                sum = accumulate(elements.begin()+j, elements.end(), 0);
                sum += accumulate(elements.begin(), elements.begin() + (i+j)-elements.size(), 0);
            }
            else{
                sum = accumulate(elements.begin()+j, elements.begin()+i+j, 0);     
            }
            s.insert(sum);
        }
    }
    return s.size();
}