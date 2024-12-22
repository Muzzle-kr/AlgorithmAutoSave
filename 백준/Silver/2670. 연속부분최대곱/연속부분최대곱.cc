#include <iostream>
#include <vector>

using namespace std;
int n;
double answer = 0;

int main() {
    cin >> n;

    vector<double> v(n);
    vector<double> dp(n, 0);
    for (int i = 0; i < n; i++) {
        double value;
        cin >> value;
        v[i] = value;
        dp[i] = value;
    }

    dp[0] = v[0];

    for (int i = 1; i < n; i++) {
        dp[i] = max(v[i], dp[i - 1] * v[i]);
        answer = max(answer, dp[i]);
    }

    printf("%.3lf\n", answer);
    return 0;
}
