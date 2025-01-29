#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void print_impossible(int idx) {
    cout << "Triangle #" << idx << endl;
    cout << "Impossible." << endl;
    cout << endl;
}

int main() {
    cout << fixed << setprecision(3);
    int idx = 1;

    while (true) {
        double a, b, c;
        cin >> a >> b >> c;

        if (a == 0 && b == 0 && c == 0) {
            return 0;
        }

        char answer;
        double length = 0.0;

        if (a == -1) {
            answer = 'a';

            if (b >= c) {
                print_impossible(idx);
                idx++;
                continue;
            }

            length = sqrt((c * c) - (b * b));
        }

        if (b == -1) {
            answer = 'b';
            if (a >= c) {
                print_impossible(idx);
                idx++;
                continue;
            }

            length = sqrt((c * c) - (a * a));
        }

        if (c == -1) {
            answer = 'c';
            length = sqrt((a * a) + (b * b));
        }

        cout << "Triangle #" << idx << endl;
        cout << answer << " = " << length << endl;
        cout << endl;

        idx++;
    }
    return 0;
}

