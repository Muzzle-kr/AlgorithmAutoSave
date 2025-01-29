#include <iostream>
#include <vector>

using namespace std;

int main() {
    unsigned long long a, b, c;
    cin >> a >> b >> c;

    unsigned long long result = a * b * c;

    string s = to_string(result);
    vector<int> v(10);

    for (int i = 0; i < s.size(); i++) {
        v[s[i] - '0'] += 1;
    }

    for (int i = 0; i < 10; i++) {
        cout << v[i] << endl;
    }

    return 0;
}
