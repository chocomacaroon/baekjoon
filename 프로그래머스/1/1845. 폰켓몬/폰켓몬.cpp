#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    set<int> s(nums.begin(), nums.end());
    if(s.size() > nums.size()/2)
        return nums.size()/2;
    return s.size();
}