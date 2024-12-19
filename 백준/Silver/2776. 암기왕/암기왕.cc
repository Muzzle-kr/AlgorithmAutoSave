#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_set>
using namespace std;

int t;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, m;
        vector<int> arr1;
        vector<int> arr2;

        cin >> n;
        unordered_set<int> check_set;
        
        for (int j = 0; j < n; j++) {
            int temp;
            cin >> temp;
            check_set.insert(temp);
        }

        sort(arr1.begin(), arr1.end());

        cin >> m;
        for (int j = 0; j < m; j++) {
            int temp;
            cin >> temp;

            if (check_set.find(temp) != check_set.end()) {
                cout << 1 << "\n";
            } else {
                cout << 0 << "\n";
            }
        }
    }
}