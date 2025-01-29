#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    vector<int> answer;
    int total = 0;

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            answer.push_back(v[i]);
            total += v[i];
            continue;
        }

        int current_number = v[i] * (i + 1) - total;
        total += current_number;
        answer.push_back(current_number);
    }

    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i] << " ";
    }
    return 0;
}