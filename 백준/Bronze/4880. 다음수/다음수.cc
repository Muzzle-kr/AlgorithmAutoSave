#include <iostream>

using namespace std;

int main() {
    while (true) {
        int a, b, c;
        cin >> a >> b >> c;

        if (a == 0 && b == 0 && c == 0) {
            return 0;
        }

        if (c - b == b - a) {
            cout << "AP " << c + (c - b) << endl;
        } else {
            cout << "GP " << c / b * c << endl;
        }
    }
}