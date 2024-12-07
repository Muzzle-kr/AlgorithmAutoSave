#include <iostream>
#include <sstream>
#include <vector>

using namespace std;



int main() {
    int n, x;
    cin >> n;

    vector<int> arr;

    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        arr.push_back(m);
    }

    cin >> x;

    sort(arr.begin(), arr.end());

    int left = 0;
    int right = n - 1;
    int answer = 0;
    while (left < right) {
        int total = arr[left] + arr[right];

        if (total > x) {
            right -= 1;
        } else if (total < x) {
            left += 1;
        } else {
            answer += 1;
            right -= 1;
        }
    }

    cout << answer << endl;
    return 0;
}
