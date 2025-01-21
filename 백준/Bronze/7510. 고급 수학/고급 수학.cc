#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        vector<int> v = { a, b, c };
        sort(v.begin(), v.end());

        int min1 = v[0];
        int min2 = v[1];
        int max = v[2];


        cout << "Scenario #" << i+1 << ":" << endl;

        if (min1*min1 + min2*min2 == max*max) {
            cout << "yes" << endl;
        } else {
            cout << "no" << endl;
        }
        cout << endl;
    }
    return 0;
}