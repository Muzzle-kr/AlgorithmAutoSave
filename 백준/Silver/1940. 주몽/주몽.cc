#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> arr;
    int result = 0;

    for (int i = 0; i < n; i++) {
        int s;
        cin >> s;
        arr.push_back(s);
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == m) {
                result++;
            }
        }
    }

    cout << result << '\n';
    return 0;
}
