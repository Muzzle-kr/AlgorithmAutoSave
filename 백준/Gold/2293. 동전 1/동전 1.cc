#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

int n, k;

int dp[100004];

int main() {
    cin >> n >> k;
    vector<int> coins(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    dp[0] = 1;

    for (int coin : coins) {
        for (int i = coin; i <= k; i++) {
            dp[i] += dp[i - coin];
        }
    }

    cout << dp[k] << endl;
    return 0;
}