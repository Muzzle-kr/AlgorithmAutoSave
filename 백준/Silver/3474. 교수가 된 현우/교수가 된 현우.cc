#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int ret2 = 0, ret5 = 0;
        int a;
        cin >> a;

        for (int j = 2; j <= a; j*=2) {
            ret2 += a / j;
        }

        for (int j = 5; j <= a; j*=5) {
            ret5 += a / j;
        }

        cout << min(ret2, ret5) << '\n';
    }
    return 0;
}