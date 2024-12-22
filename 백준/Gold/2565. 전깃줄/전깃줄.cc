#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    double answer = 0;

    cin >> n;

    vector<pair<int, int>> v;

    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        v.push_back(make_pair(start, end));
    }
    sort(v.begin(), v.end());
    int len = 0;

    vector<int> lis;

    for (auto const & iterator : v) {
        int end_value = iterator.second;
        auto it = lower_bound(lis.begin(), lis.end(), end_value);

        if (it == lis.end()) {
            lis.push_back(end_value);
        } else {
            *it = end_value;
        }
    }

    cout << n - lis.size() << endl;
    return 0;
}
