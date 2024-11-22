#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    int count = 0;

    for (int i = 665; i < 1000000000; i++) {
        if (to_string(i).find("666") != string::npos) {
            count++;
        }

        if (count == n) {
            cout << i << endl;
            return 0;
        }
    }
    return 0;
}
