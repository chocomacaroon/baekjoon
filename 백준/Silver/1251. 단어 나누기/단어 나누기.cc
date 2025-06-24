#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string s;
    cin >> s;
    string answer = "";

    size_t n = s.size();

    for (size_t i = 1; i < n - 1; i++) {
        for (size_t j = i + 1; j < n; j++) {
            string s1 = s.substr(0, i);
            string s2 = s.substr(i, j - i);
            string s3 = s.substr(j);

            reverse(s1.begin(), s1.end());
            reverse(s2.begin(), s2.end());
            reverse(s3.begin(), s3.end());

            string tmp = s1 + s2 + s3;

            if (answer.empty() || tmp < answer) {
                answer = tmp;
            }
        }
    }

    cout << answer << endl;
}
