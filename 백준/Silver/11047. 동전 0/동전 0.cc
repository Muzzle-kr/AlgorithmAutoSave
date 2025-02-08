#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sort(v.begin(), v.end(), greater<int>());

    int answer = 0;

    for (int i = 0; i < n; i++) {
        if (k / v[i] >= 1) {
            answer += k / v[i];
            k %= v[i];
        }
    }
    cout << answer << endl;
    return 0;
}