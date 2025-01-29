#include <iostream>
#include <vector>
#include <sstream>
#include <climits>

using namespace std;

int main() {
    int year, m, d;
    cin >> year >> m >> d;

    int n_year, n_m, n_d;
    cin >> n_year >> n_m >> n_d;

    int man_age = 0, sae_age = 1, yeon_age = 0;

    man_age = n_year - year;
    if ((n_m == m && n_d < d) || (n_m < m)) {
        man_age -= 1;
    }

    sae_age += n_year - year;
    yeon_age = n_year - year;

    cout << man_age << endl;
    cout << sae_age << endl;
    cout << yeon_age << endl;
    return 0;
}
