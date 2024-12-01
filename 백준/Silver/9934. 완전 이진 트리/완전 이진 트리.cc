#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int k = 0;
int n = 0;
vector<int> arr;

void dfs(int depth, int start, int end, auto & answer) {
    if (depth == k) {
        return;
    }

    if (start == end) {
        answer[depth].push_back(arr[start]);
        return;
    }

    int center = (start + end) / 2;
    answer[depth].push_back(arr[center]);
    dfs(depth + 1, start, center - 1, answer);
    dfs(depth + 1, center + 1, end, answer);
}
int main() {
    cin >> k;
    n = pow(2, k) - 1;

    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        arr.push_back(m);
    }

    vector<vector<int>> answer(k, vector<int>());
    dfs(0, 0, n - 1, answer);

    for (int i = 0; i < k; i++) {
        for (int n : answer[i]) {
            cout << n << " ";
        }
        cout << endl;
    }
    return 0;
}