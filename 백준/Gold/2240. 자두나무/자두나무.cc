#include <iostream>
#include <cstring>

int dp[1004][2][34], b[1004];
int n, m;

using namespace std;

int go(int index, int tree, int move) {
    if (move < 0) return -1e9;
    if (index == n) return 0;
    int &ret = dp[index][tree][move];
    if (~ret) return ret;

    return ret = max(go(index + 1, tree^1, move - 1), go(index + 1, tree, move)) + (tree == b[index] - 1);
}
int main() {

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    memset(dp, -1, sizeof(dp));
    cout << max(go(0, 0, m), go(0, 1, m - 1)) << '\n';
    return 0;
}