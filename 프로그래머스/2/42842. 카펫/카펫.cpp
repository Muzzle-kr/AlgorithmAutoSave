#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int total = brown + yellow;

    int min_diff = 1e9;
    
    for (int i = 1; i < total / 2 + 1; i++) {
        if (total % i == 0) {
            int a = i;
            int b = total / i;

            if (a >= b && (a - 2) * (b - 2) == yellow) {
                if (min_diff > a - b) {
                    min_diff = a - b;
                    answer = {a, b};
                }
            }
        }
    }

    return answer;
}