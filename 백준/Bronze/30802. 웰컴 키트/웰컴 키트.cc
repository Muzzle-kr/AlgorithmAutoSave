#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> tshirts;

    for (int i = 0; i < 6; i++) {
        int t;
        cin >> t;
        tshirts.push_back(t);
    }

    int t, p;
    cin >> t >> p;
    int t_count = 0, p_count = 0;

    for (int i = 0; i < 6; i++) {
        if (tshirts[i] % t == 0) {
            t_count += tshirts[i] / t;
        } else {
            t_count += tshirts[i] / t + 1;
        }
    }

    p_count += n / p;
    cout << t_count << endl;
    cout << p_count << " " << n % p << endl;

    return 0;
}