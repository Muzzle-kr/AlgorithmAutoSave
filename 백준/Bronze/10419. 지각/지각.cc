#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        for (int j = 0; j < 101; j++) {
            if (j * j + j > x) {
                cout << j-1 << " ";
                break;
            }
        }
    }
    return 0;
}