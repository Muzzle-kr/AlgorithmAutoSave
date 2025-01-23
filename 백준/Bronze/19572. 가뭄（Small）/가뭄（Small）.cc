#include <iostream>

using namespace std;

int main() {
    float d1, d2, d3;
    cin >> d1 >> d2 >> d3;

    float b = (d3 - d2 + d1) / 2.0f;
    float a = d1 - b;
    float c = d2 - d1 + b;

    if (a > 0 && b > 0 && c > 0) {
        cout << 1 << endl;
        cout << fixed;
        cout.precision(1);
        cout << a << " " << b << " " << c << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}