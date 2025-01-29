#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;


    for (int i = 0; i < n; i++) {
        double t, length, a, b, fly;
        cin >> t >> length >> a >> b >> fly;

        double need_time = length / (a + b);
        double answer = need_time * fly;

        cout << fixed << setprecision(6);
        cout << t << " " << answer << endl;
    }


    return 0;
}