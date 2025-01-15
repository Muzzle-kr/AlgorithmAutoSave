#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int empty_bottle = a + b;
    int answer = 0;

    while (empty_bottle >= c) {
        empty_bottle -= c;
        empty_bottle++;
        answer++;
    }
    cout << answer << endl;
    return 0;
}