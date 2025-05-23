// #include <string>
// #include <vector>
// #include <cmath>

// using namespace std;

// long long solution(long long n) {
//     long long answer = -1;
//     if(sqrt(n)*sqrt(n)==n){
//         return (sqrt(n)+1)*(sqrt(n)+1);
//     }
//     return answer;
// }
#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long root = sqrt(n);
    if (root * root == n) {
        return (root + 1) * (root + 1);
    } else {
        return -1;
    }
}
