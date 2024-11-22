#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> result = {666};

bool includeDemonNumber(string s) {
    return s.find("666") != string::npos;
}

int main() {
    int n;
    cin >> n;

    if (n == 0) {
        cout << result[0] << endl;
        return 0;
    }

    for (int i = 1; i < n; i++) {
        int start = result[i-1] + 1;

        while (true) {
            if (includeDemonNumber(to_string(start))) {
                result.push_back(start);
                break;
            }
            start++;
        }
    }

    cout << result[n-1] << endl;
    return 0;
}
