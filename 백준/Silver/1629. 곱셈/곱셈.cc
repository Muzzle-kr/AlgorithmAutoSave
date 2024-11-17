#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

long long power(long long a, long long b, long long c) {
    if (b == 0) return 1;
    if (b == 1) return a % c;

    long long half = power(a, b / 2, c);
    half = (half * half) % c;

    if (b % 2 == 0) {
        return half;
    } else {
        return (half * a) % c;
    }
}

int main() {
    long long a, b, c;
    cin >> a >> b >> c;

    cout << power(a, b, c) << endl;
    return 0;
}
