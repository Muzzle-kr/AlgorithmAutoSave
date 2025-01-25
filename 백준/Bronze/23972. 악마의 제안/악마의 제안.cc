#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k = 0;
    cin >> n >> k;

    int answer = -1;
    for (int i = 1; i <= 200000000; i++) {
        if (i * k >= n + i) {
            answer = n + i;
            break;
        }
    }

    cout << answer << endl;
    return 0;
}