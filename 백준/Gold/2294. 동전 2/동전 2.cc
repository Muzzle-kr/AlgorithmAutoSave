#include <iostream>
#include <vector>
#include <tuple>
#include <cstring>

using namespace std;

int calculate(int current_coin, int n, int k, vector<int> & a, vector<int> & dp) {    
    if (current_coin == k) {
        return dp[current_coin];
    }
    
    int count = dp[current_coin];

    for (int i = 0; i < n; i++) {
        int coin = a[i];
        
        if (current_coin + coin > k) {
            continue;
        }

        if (dp[current_coin + coin] > count + 1) {
            dp[current_coin + coin] = count + 1;
            calculate(current_coin + coin, n, k, a, dp);
        }
    }
    return dp[k];
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int ans = 0;

    vector<int> dp(k + 1, 1e9);
    dp[0] = 0;
    
    int result = calculate(0, n, k, a, dp);
    
    if (result == 1e9) {
        result = -1;
    }
    
    cout << result << endl;
    return 0;
}