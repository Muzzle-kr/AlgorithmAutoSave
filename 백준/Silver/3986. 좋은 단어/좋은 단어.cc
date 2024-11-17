#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    int result = 0;

    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;

        vector<char> arr;

        for (char w : word) {
            if (!arr.empty() && arr.back() == w) {
                arr.pop_back();
            } else {
                arr.push_back(w);
            }
        }

        if (arr.empty()) {
            result++;
        }
    }

    cout << result << endl;
    return 0;
}
