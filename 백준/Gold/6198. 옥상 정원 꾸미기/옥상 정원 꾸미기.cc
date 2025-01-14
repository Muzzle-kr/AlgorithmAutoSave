#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        v.push_back(x);
    }
    vector<int> building_stack;
    vector<int> empty_stack;
    long long answer = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                answer++;
            } else {
                break;
            }
        }
    }
    cout << answer << endl;
    return 0;
}