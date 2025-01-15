#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    while (true) {
        int x;
        cin >> x;

        if (x == 0) {
            break;
        }

        if (x % n == 0) {
            cout << x << " is a multiple of " << n << "." << endl;
        } else {
            cout << x << " is NOT a multiple of " << n << "." << endl;
        }
    }

    return 0;
}