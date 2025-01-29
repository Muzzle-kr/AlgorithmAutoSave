#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << fixed << setprecision(9);
    double e = 0.0;
    double factorial = 1.0;

    cout << "n e" << endl;
    cout << "- -----------" << endl;
    cout << "0 1" << endl;
    cout << "1 2" << endl;
    cout << "2 2.5" << endl;
    for (int n = 0; n <= 9; n++) {
        if (n > 0) {
            factorial *= n;
        }

        e += 1.0 / factorial;

        if (n < 3) {
            continue;
        }

        cout << n << " " << e << endl;
    }

    return 0;
}