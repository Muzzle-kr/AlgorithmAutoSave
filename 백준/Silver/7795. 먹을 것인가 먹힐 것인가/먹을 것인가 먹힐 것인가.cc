#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;

        vector<int> arr_n(n);
        vector<int> arr_m(m);

        for (int j = 0; j < n; j++) {
            cin >> arr_n[j];
        }

        for (int j = 0; j < m; j++) {
            cin >> arr_m[j];
        }

        sort(arr_n.begin(), arr_n.end());
        sort(arr_m.begin(), arr_m.end());

        int answer = 0;
        for (int j = 0; j < n; j++) {
            int x = arr_n[j];

            int index = (lower_bound(arr_m.begin(), arr_m.end(), x) - arr_m.begin());
            answer += index;
        }
        cout << answer << "\n";
    }
    return 0;
}