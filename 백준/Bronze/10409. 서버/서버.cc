#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, t;
    cin >> n >> t;

    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        v[i] = x;
    }

    int total = 0;
    int count = 0;

    for (int i = 0; i < n; i++) {
        if (total + v[i] > t) {
            break;
        }

        total += v[i];
        count++;
    }
    
    cout << count << endl;
    return 0;
}