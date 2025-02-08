#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

int main() {
    int n;
    long long m; 
    cin >> n >> m;
    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sort(v.begin(), v.end());

    int left = 0;
    int right = v[n-1];

    int answer = 0;
    while (left <= right) {
        int saw = (left + right) / 2;

        long long total = 0; 

        for (int tree : v) {
            total += max(tree - saw, 0);
        }

        if (total >= m) {
            answer = saw;
            left = saw + 1;
        } else {
            right = saw - 1;
        }
    }
    cout << answer << endl;
    return 0;
}
