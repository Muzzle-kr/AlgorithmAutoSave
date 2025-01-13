#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> v(1004, vector<int>(1004, -1));

    for (int i = 0; i < n; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        for (int k = a; k < a + c; k++) {
            for (int l = b; l < b + d; l++) {
                v[k][l] = i;
            }
        }
    }

    vector<int> area(n, 0);
    for (int j = 0; j < 1004; j++) {
        for (int k = 0; k < 1004; k++) {
            if (v[j][k] != -1) {
                area[v[j][k]]++;
            }
        }
    }


    for (int i = 0; i < n; i++) {
        cout << area[i] << endl;
    }

    return 0;
}