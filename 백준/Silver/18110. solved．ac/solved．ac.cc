#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> level;

    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        level.push_back(t);
    }

    sort(level.begin(), level.end());

    long long t = llround(n * 0.15);

    int total_level = 0;
    for (int i = t; i < n - t; i++) {
        total_level += level[i];
    }

    double level_count = n - 2 * t;
    int answer = lround(total_level / level_count);
    cout << answer << endl;
    return 0;
}