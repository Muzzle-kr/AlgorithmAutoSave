#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> dp(n + 2, 0);

    dp[0] = 0;
    dp[1] = 0;
    dp[2] = 3;

    if (n <= 2) {
        cout << dp[n] << endl;
        return 0;
    }

    if (n % 2 == 1) {
        cout << 0 << endl;
        return 0;
    }

    for (int i = 4; i < n + 1; i += 2) {
        dp[i] = dp[i-2] * 3;

        for (int j = 4; j <= i; j += 2) {
            dp[i] += dp[i-j] * 2;
        }
        dp[i] += 2;
    }

    cout << dp[n] << endl;
    return 0;
}
