#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, x, k;
    cin >> n >> x >> k;

    vector<int> v(n + 1);
    v[x] = 1;

    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;

        int tmp = v[b];
        v[b] = v[a];
        v[a] = tmp;
    }

    int answer = 0;
    for (int i = 1; i <= n; i++) {
        if (v[i] == 1) {
            answer = i;
            break;
        }
    }

    cout << answer << endl;
    return 0;
}