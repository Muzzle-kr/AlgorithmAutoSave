#include <iostream>

using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;

    long long left = 0, right = 1e9;
    long long win_rate = b * 100 / a;

    long long answer = -1;

    while (left <= right) {
        long long mid = (left + right) / 2;
        long long new_a = a + mid;
        long long new_b = b + mid;

        int new_win_rate = new_b * 100 / new_a;

        if (new_win_rate > win_rate) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    cout << answer << endl;
    return 0;
}
